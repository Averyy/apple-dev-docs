# Importing Bézier path data into PencilKit

**Framework**: PencilKit

Convert existing Bézier-based stroke data into PencilKit drawing strokes.

#### Overview

If your app handles drawing data as Bézier paths, such as when you import an existing file format, interface with a third-party library, or store drawing data in your own data model, you can convert those Bézier paths directly into PencilKit drawing strokes and adopt PencilKit as your rendering engine without discarding your existing data.

PencilKit uses a stroke format optimized for Apple Pencil input, represented by [`PKStroke`](pkstroke-swift.struct.md), which differs from the Bézier path format that Core Graphics and other frameworks use. Because the two formats represent curves differently, the conversion is an approximation. After you convert your stroke data, review the results to confirm the strokes look as you expect.

#### Convert a B%c3%a9zier Path to a Stroke

To convert a Bézier path, initialize a [`PKStrokePath`](pkstrokepath-swift.struct.md) from a [`CGPath`](https://developer.apple.com/documentation/CoreGraphics/CGPath) using [`init(bezierPath:creationDate:pointProvider:)`](pkstrokepath-swift.struct/init(bezierpath:creationdate:pointprovider:).md). Because a Bézier path describes only the shape of a curve and not the per-point properties PencilKit uses for rendering, such as pressure, opacity, and size, you supply those values through the `pointProvider` closure, which the system calls once for each point in the resulting path.

> ❗ **Important**: [`init(bezierPath:creationDate:pointProvider:)`](pkstrokepath-swift.struct/init(bezierpath:creationdate:pointprovider:).md) only converts the first subpath. Split each subpath into its own [`CGPath`](https://developer.apple.com/documentation/CoreGraphics/CGPath) before converting.

To call the initializer, you supply two values alongside the Bézier path: a `creationDate` for the stroke, and a `pointProvider` closure that returns rendering properties for each point. The `creationDate` is the start time of the stroke. Pass a timestamp from your source data if one exists, or use [`Date`](https://developer.apple.com/documentation/Foundation/Date)() for the current time.

The number of points PencilKit derives from your Bézier path may differ from the number of control points in the original. Use `index` and `pointCount` to calculate values that vary along the stroke rather than mapping points one-to-one from your source data.

The initializer calls `pointProvider` once for each derived point, passing a [`PKStrokePath.ConvertedBezierPoint`](pkstrokepath-swift.struct/convertedbezierpoint.md) with the following values:

- [`location`](pkstrokepath-swift.struct/convertedbezierpoint/location.md): The position of the derived B-spline control point, which you pass directly to [`PKStrokePoint`](pkstrokepoint-swift.struct.md).
- [`index`](pkstrokepath-swift.struct/convertedbezierpoint/index.md) and [`pointCount`](pkstrokepath-swift.struct/convertedbezierpoint/pointcount.md): `index` is the zero-based position of the control point in the derived path, and `pointCount` is the total number of control points. Divide one by the other to calculate a progress value between 0 and 1 for properties that vary along the stroke.
- [`bezierSegmentIndex`](pkstrokepath-swift.struct/convertedbezierpoint/beziersegmentindex.md): The index of the original Bézier segment that this derived control point maps to. Use this value if your source data stores per-segment properties like color or width.

PencilKit sets `location` from the Bézier path geometry, but you define all other properties — such as `size`, `opacity`, and `force` — in your `pointProvider` closure. For the following properties, consider whether your source data includes values to use rather than a fixed default:

- [`timeOffset`](pkstrokepoint-swift.struct/timeoffset.md): The time in seconds from the stroke’s `creationDate` to this derived control point. The example below distributes time evenly along the stroke based on index position, giving earlier points smaller offsets and later points larger ones. If your source data includes per-point or per-segment timestamps, use those elapsed times instead.
- [`azimuth`](pkstrokepoint-swift.struct/azimuth.md) and [`altitude`](pkstrokepoint-swift.struct/altitude.md): These properties describe the orientation of an Apple Pencil. For imported data that doesn’t include pencil orientation, use reasonable values instead. For example, an altitude of `.pi / 4` matches how most people naturally hold a pencil. Because azimuth only affects rendering once the pencil is tilted, choose a value that fits your ink and app rather than relying on a single default.

The following example shows a complete conversion from a [`CGPath`](https://developer.apple.com/documentation/CoreGraphics/CGPath) to a `PKStroke`, using `index` and `pointCount` to calculate `timeOffset` and applying uniform values for all other properties:

```swift
func makeStroke(from bezierPath: CGPath, ink: PKInk) -> PKStroke {
    let path = PKStrokePath(
        bezierPath: bezierPath,
        creationDate: Date(),
        pointProvider: { convertedPoint in
            let progress = CGFloat(convertedPoint.index) / CGFloat(convertedPoint.pointCount)
            return PKStrokePoint(
                location: convertedPoint.location,
                timeOffset: 0.5 * progress,
                size: CGSize(width: 3.0, height: 3.0),
                opacity: 1.0,
                force: 1.0,
                azimuth: .pi,
                altitude: .pi / 4,
                secondaryScale: 1.0,
                threshold: 0.0
            )
        }
    )
    return PKStroke(ink: ink, path: path)
}
```

#### Save and Load Pencilkit Strokes in a B%c3%a9zier File Format

If you want to keep Bézier paths as your file format after adopting PencilKit, you can export strokes back to Bézier paths for saving and reload them with full fidelity. Use [`bezierRepresentation`](pkstrokepath-swift.struct/bezierrepresentation.md) to export a stroke path to a [`CGPath`](https://developer.apple.com/documentation/CoreGraphics/CGPath) for saving, then [`init(bezierPath:creationDate:pointProvider:)`](pkstrokepath-swift.struct/init(bezierpath:creationdate:pointprovider:).md) to load it back.

A Bézier path stores only the shape of the curve and doesn’t include properties like size, opacity, and force. When exporting a PencilKit stroke, save those properties separately for each point so you can reconstruct the full stroke when loading back.

The following example shows how to save these additional properties alongside the Bézier path:

```swift
struct SavedPoint: Codable {
    let timeOffset: TimeInterval
    let size: CGSize
    let opacity: CGFloat
    let force: CGFloat
    let azimuth: CGFloat
    let altitude: CGFloat
    let secondaryScale: CGFloat
    let threshold: CGFloat

    init(_ point: PKStrokePoint) {
        timeOffset = point.timeOffset
        size = point.size
        opacity = point.opacity
        force = point.force
        azimuth = point.azimuth
        altitude = point.altitude
        secondaryScale = point.secondaryScale
        threshold = point.threshold
    }
}

let bezierPath = stroke.path.bezierRepresentation
let savedPoints = stroke.path.map { SavedPoint($0) }
```

When loading back a path exported with [`bezierRepresentation`](pkstrokepath-swift.struct/bezierrepresentation.md), the number of control points is guaranteed to match the original stroke’s point count — so you can look up each point’s saved data by index:

```swift
let restoredPath = PKStrokePath(
    bezierPath: bezierPath,
    creationDate: Date(),
    pointProvider: { convertedPoint in
        let saved = savedPoints[convertedPoint.index]
        return PKStrokePoint(
            location: convertedPoint.location,
            timeOffset: saved.timeOffset,
            size: saved.size,
            opacity: saved.opacity,
            force: saved.force,
            azimuth: saved.azimuth,
            altitude: saved.altitude,
            secondaryScale: saved.secondaryScale,
            threshold: saved.threshold
        )
    }
)
```

#### Add the Converted Strokes to a Drawing

[`PKDrawing`](pkdrawing-swift.struct.md) holds all the strokes that appear in a canvas. After converting your strokes, set the [`strokes`](pkdrawing-swift.struct/strokes.md) property on a new drawing and assign it to your [`PKCanvasView`](pkcanvasview.md). This replaces any existing content in the canvas with your imported strokes. The following example converts a collection of legacy paths to strokes and assigns them to a canvas:

```swift
let strokes = legacyDocument.paths.map { path in
    makeStroke(from: path.cgPath, ink: PKInk(inkType: .pen, color: path.color))
}

var drawing = PKDrawing()
drawing.strokes = strokes
canvasView.drawing = drawing
```

## See Also

- [Drawing with PencilKit](drawing-with-pencilkit.md)
  Add expressive, low-latency drawing to your app using PencilKit.
- [Customizing Scribble with Interactions](customizing-scribble-with-interactions.md)
  Enable writing on a non-text-input view by adding interactions.
- [Inspecting, Modifying, and Constructing PencilKit Drawings](inspecting-modifying-and-constructing-pencilkit-drawings.md)
  Score users’ ability to match PencilKit drawings generated from text, by accessing the strokes and points inside PencilKit drawings.
- [Controlling stroke rendering for animation and editing](controlling-stroke-rendering-for-animation-and-editing.md)
  Slice, animate, and blend PencilKit strokes in code, while keeping grain texture and wet ink intact.
- [class PKCanvasView](pkcanvasview.md)
  A view that captures Apple Pencil input and displays the rendered results in an iOS app.
- [struct PKDrawing](pkdrawing-swift.struct.md)
  A structure representing the drawing information captured by a canvas view.
- [struct PKStroke](pkstroke-swift.struct.md)
  A structure that represents the paths, boundaries, and other properties of a stroke drawn on a canvas.
- [struct PKStrokePath](pkstrokepath-swift.struct.md)
  A structure that captures the components of a stroke and provides methods to find and interpolate points along the stroke’s path.
- [struct PKStrokePoint](pkstrokepoint-swift.struct.md)
  A structure that represents the properties of a specific point along a stroke’s path.
- [struct PKInk](pkink-swift.struct.md)
  A structure that represents an ink that specifies its type, color, and width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/importing-external-drawing-data-into-pencilkit)*