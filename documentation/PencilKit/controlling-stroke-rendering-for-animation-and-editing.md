# Controlling stroke rendering for animation and editing

**Framework**: PencilKit

Slice, animate, and blend PencilKit strokes in code, while keeping grain texture and wet ink intact.

#### Overview

Use [`substroke(range:)`](pkstroke-swift.struct/substroke(range:).md), [`PKStroke.RenderState`](pkstroke-swift.struct/renderstate-swift.struct.md), and [`renderGroupID`](pkstroke-swift.struct/rendergroupid.md) to control how strokes look when you create or edit them in code. With these APIs, you can play back a recorded drawing by revealing each stroke as it was originally drawn, keep grain texture in place when you edit a stroke, and make marker strokes blend together the same way they do when someone draws them.

When you create or modify strokes in code, PencilKit doesn’t automatically carry visual details, for example, grain-texture position and wet-ink grouping, into the new stroke. Learn how to set those details explicitly so your strokes look the same as strokes drawn naturally on the canvas.

#### Slice a Stroke at Any Point

`PKStrokePath` lets you slice a path at any position, not just at whole-number positions. Specify the slice as a range where `0` is the start, `count - 1` is the end, and values like `2.5` fall between two points.

```swift
let path = stroke.path

// Extract the middle section of a path.
let middleSection = path[2.5...7.0]
```

To slice a full stroke, use [`substroke(range:)`](pkstroke-swift.struct/substroke(range:).md). It keeps the ink and rendering details intact so the sliced portion looks the same as it did in the original stroke.

```swift
let firstHalf = stroke.substroke(range: 0...CGFloat(stroke.path.count - 1) * 0.5)
```

#### Animate a Stroke Reveal

A common effect in drawing apps is showing a stroke appearing gradually, which is useful for playback features, tutorials, or animated transitions.

Use [`substroke(range:)`](pkstroke-swift.struct/substroke(range:).md) rather than slicing the path directly. It preserves the ink and rendering details of the original stroke, so each frame looks exactly as it did at that point in the original drawing.

```swift
func animateStrokeReveal(_ stroke: PKStroke, progress: CGFloat) -> PKStroke {
    let endPoint = CGFloat(stroke.path.count - 1) * progress.clamped(to: 0...1)
    return stroke.substroke(range: 0...endPoint)
}
```

To drive the animation, update your drawing on each frame:

```swift
func startRevealAnimation(for stroke: PKStroke) {
    var progress: CGFloat = 0

    Timer.scheduledTimer(withTimeInterval: 1.0 / 60.0, repeats: true) { [weak self] timer in
        guard let self else { timer.invalidate(); return }
        progress = min(progress + 0.02, 1.0)

        var drawing = self.canvasView.drawing
        drawing.strokes = [animateStrokeReveal(stroke, progress: progress)]
        self.canvasView.drawing = drawing

        if progress >= 1.0 {
            timer.invalidate()
        }
    }
}
```

#### Preserve Rendering State When Editing Strokes

When you construct a new stroke based on an existing one, for example, after changing its path, copy the [`renderState`](pkstroke-swift.struct/renderstate-swift.property.md) from the original. Dropping it can cause the new stroke to look different from the original even when the path and ink are the same.

```swift
let editedStroke = PKStroke(
    ink: originalStroke.ink,
    path: newPath,
    transform: originalStroke.transform,
    renderState: originalStroke.renderState
)
```

> **Note**: [`PKStroke.RenderState`](pkstroke-swift.struct/renderstate-swift.struct.md) includes [`grainOffset`](pkstroke-swift.struct/renderstate-swift.struct/grainoffset.md), which anchors the grain texture for inks like crayon, as well as opaque properties for other ink types such as pencil. If [`renderState`](pkstroke-swift.struct/renderstate-swift.property.md) is non-nil, pass it along whenever the new stroke is meant to look like the original.

#### Composite Marker Strokes As Wet Ink

When people draw multiple strokes with compatible inks, such as marker and watercolor, in quick succession, PencilKit blends them where they overlap, rather than layering them. For this to work, PencilKit needs data on which strokes belong together.

When your app creates a group of strokes that need to blend this way, assign the same [`renderGroupID`](pkstroke-swift.struct/rendergroupid.md) to all of them. Generate a single `UUID` for the group and pass it to each stroke:

```swift
func makeWetInkStrokes(paths: [PKStrokePath], ink: PKInk) -> [PKStroke] {
    let groupID = UUID()

    return paths.map { path in
        PKStroke(
            ink: ink,
            path: path,
            renderGroupID: groupID
        )
    }
}
```

Contiguous strokes with the same [`renderGroupID`](pkstroke-swift.struct/rendergroupid.md) blend together as wet ink. Strokes without a `renderGroupID`, or with a different ID, render independently.

> **Note**: Wet-ink blending is only visible with inks that support it, such as marker. Assigning a [`renderGroupID`](pkstroke-swift.struct/rendergroupid.md) to other ink types has no effect on their appearance.

#### Combine Techniques for Animated Playback

These techniques work together. Consider an app that plays back a sequence of handwritten marker strokes — each stroke needs to appear gradually while keeping the wet-ink blending intact. Pass the set of strokes and a progress value from `0` to `1`, and the function returns how much of each stroke to show at that point in the playback:

```swift
func animateGroupReveal(strokes: [PKStroke], progress: CGFloat) -> [PKStroke] {
    let totalPoints = strokes.reduce(0) { $0 + $1.path.count }
    let targetPoints = Int(CGFloat(totalPoints) * progress)
    var remaining = targetPoints
    var result: [PKStroke] = []

    for stroke in strokes {
        if remaining <= 0 { break }
        let strokePoints = stroke.path.count
        if remaining >= strokePoints {
            result.append(stroke)
            remaining -= strokePoints
        } else {
            result.append(stroke.substroke(range: 0...CGFloat(remaining - 1)))
            remaining = 0
        }
    }

    return result
}
```

Because [`substroke(range:)`](pkstroke-swift.struct/substroke(range:).md) preserves the [`renderGroupID`](pkstroke-swift.struct/rendergroupid.md) from the original stroke, the marker strokes still blend together as wet ink when they appear during playback.

## See Also

- [Drawing with PencilKit](drawing-with-pencilkit.md)
  Add expressive, low-latency drawing to your app using PencilKit.
- [Customizing Scribble with Interactions](customizing-scribble-with-interactions.md)
  Enable writing on a non-text-input view by adding interactions.
- [Inspecting, Modifying, and Constructing PencilKit Drawings](inspecting-modifying-and-constructing-pencilkit-drawings.md)
  Score users’ ability to match PencilKit drawings generated from text, by accessing the strokes and points inside PencilKit drawings.
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

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/controlling-stroke-rendering-for-animation-and-editing)*