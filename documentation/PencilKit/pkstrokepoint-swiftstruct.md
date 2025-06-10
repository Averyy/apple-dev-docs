# PKStrokePoint

**Framework**: PencilKit  
**Kind**: struct

A structure that represents the properties of a specific point along a stroke’s path.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct PKStrokePoint
```

## Topics

### Creating a stroke point object
- [init(location: CGPoint, timeOffset: TimeInterval, size: CGSize, opacity: CGFloat, force: CGFloat, azimuth: CGFloat, altitude: CGFloat)](pkstrokepoint-swift.struct/init(location:timeoffset:size:opacity:force:azimuth:altitude:).md)
  Creates a new point with the provided properties.
- [init(location: CGPoint, timeOffset: TimeInterval, size: CGSize, opacity: CGFloat, force: CGFloat, azimuth: CGFloat, altitude: CGFloat, secondaryScale: CGFloat)](pkstrokepoint-swift.struct/init(location:timeoffset:size:opacity:force:azimuth:altitude:secondaryscale:).md)
### Getting the point’s location
- [var location: CGPoint](pkstrokepoint-swift.struct/location.md)
  The location of this point.
- [var timeOffset: TimeInterval](pkstrokepoint-swift.struct/timeoffset.md)
  The time offset since the start of the stroke path in seconds.
### Getting the point’s touch data
- [var altitude: CGFloat](pkstrokepoint-swift.struct/altitude.md)
  The altitude of this point in radians.
- [var azimuth: CGFloat](pkstrokepoint-swift.struct/azimuth.md)
  The azimuth of this point in radians.
- [var force: CGFloat](pkstrokepoint-swift.struct/force.md)
  The amount of force applied by the touch.
### Getting the point’s drawing data
- [var size: CGSize](pkstrokepoint-swift.struct/size.md)
  The size of this point.
- [var opacity: CGFloat](pkstrokepoint-swift.struct/opacity.md)
  Opacity of the point.
- [var secondaryScale: CGFloat](pkstrokepoint-swift.struct/secondaryscale.md)
### Using reference types
- [class PKStrokePointReference](pkstrokepointreference.md)
  A class that represents the properties of a specific point along a stroke’s path.
### Initializers
- [init(location: CGPoint, timeOffset: TimeInterval, size: CGSize, opacity: CGFloat, force: CGFloat, azimuth: CGFloat, altitude: CGFloat, secondaryScale: CGFloat, threshold: CGFloat)](pkstrokepoint-swift.struct/init(location:timeoffset:size:opacity:force:azimuth:altitude:secondaryscale:threshold:).md)
  Create a new point with the provided properties.
### Instance Properties
- [var threshold: CGFloat](pkstrokepoint-swift.struct/threshold.md)
  The threshold for clipping the stroke rendering.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)

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
- [struct PKInk](pkink-swift.struct.md)
  A structure that represents an ink that specifies its type, color, and width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepoint-swift.struct)*