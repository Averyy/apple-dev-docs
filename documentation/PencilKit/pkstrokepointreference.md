# PKStrokePointReference

**Framework**: PencilKit  
**Kind**: class  
**Role**: Class

A class that represents the properties of a specific point along a stroke’s path.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class PKStrokePointReference
```

```objc
@interface PKStrokePoint : NSObject
```

## Topics

### Creating a stroke point object
- [init(location: CGPoint, timeOffset: TimeInterval, size: CGSize, opacity: CGFloat, force: CGFloat, azimuth: CGFloat, altitude: CGFloat)](./pkstrokepointreference/init%28location,timeoffset,size,opacity,force,azimuth,altitude%29.md)
  Creates a new point with the provided properties.
- [init(location: CGPoint, timeOffset: TimeInterval, size: CGSize, opacity: CGFloat, force: CGFloat, azimuth: CGFloat, altitude: CGFloat, secondaryScale: CGFloat)](./pkstrokepointreference/init%28location,timeoffset,size,opacity,force,azimuth,altitude,secondaryscale%29.md)
### Getting the point’s location
- [var location: CGPoint](./pkstrokepointreference/location.md)
  The location of this point.
- [var timeOffset: TimeInterval](./pkstrokepointreference/timeoffset.md)
  The time offset since the start of the stroke path in seconds.
### Getting the point’s touch data
- [var altitude: CGFloat](./pkstrokepointreference/altitude.md)
  The altitude of this point in radians.
- [var azimuth: CGFloat](./pkstrokepointreference/azimuth.md)
  The azimuth of this point in radians.
- [var force: CGFloat](./pkstrokepointreference/force.md)
  The amount of force applied by the touch.
### Getting the point’s drawing data
- [var size: CGSize](./pkstrokepointreference/size.md)
  The size of the point.
- [var opacity: CGFloat](./pkstrokepointreference/opacity.md)
  Opacity of the point.
- [var secondaryScale: CGFloat](./pkstrokepointreference/secondaryscale.md)
### Initializers
- [init(location: CGPoint, timeOffset: TimeInterval, size: CGSize, opacity: CGFloat, force: CGFloat, azimuth: CGFloat, altitude: CGFloat, secondaryScale: CGFloat, threshold: CGFloat)](./pkstrokepointreference/init%28location,timeoffset,size,opacity,force,azimuth,altitude,secondaryscale,threshold%29.md)
  Creates a stroke point with the specified properties, including a rendering threshold.
- [init(location: CGPoint, timeOffset: TimeInterval, size: CGSize, opacity: CGFloat, force: CGFloat, azimuth: CGFloat, altitude: CGFloat, secondaryScale: CGFloat, threshold: CGFloat, lateralJitter: CGFloat)](./pkstrokepointreference/init%28location,timeoffset,size,opacity,force,azimuth,altitude,secondaryscale,threshold,lateraljitter%29.md)
  Creates a stroke point with the specified properties, including lateral jitter.
### Instance Properties
- [var lateralJitter: CGFloat](./pkstrokepointreference/lateraljitter.md)
  The amount of lateral particle jitter at the stroke edge for supported inks.
- [var threshold: CGFloat](./pkstrokepointreference/threshold.md)
  The alpha threshold for clipping the stroke rendering for supported inks.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Canvas
- [Drawing with PencilKit](./drawing-with-pencilkit.md)
  Add expressive, low-latency drawing to your app using PencilKit.
- [Customizing Scribble with Interactions](./customizing-scribble-with-interactions.md)
  Enable writing on a non-text-input view by adding interactions.
- [Inspecting, Modifying, and Constructing PencilKit Drawings](./inspecting-modifying-and-constructing-pencilkit-drawings.md)
  Score users’ ability to match PencilKit drawings generated from text, by accessing the strokes and points inside PencilKit drawings.
- [Importing Bézier path data into PencilKit](./importing-external-drawing-data-into-pencilkit.md)
  Convert existing Bézier-based stroke data into PencilKit drawing strokes.
- [Controlling stroke rendering for animation and editing](./controlling-stroke-rendering-for-animation-and-editing.md)
  Slice, animate, and blend PencilKit strokes in code, while keeping grain texture and wet ink intact.
- [PKCanvasView](./pkcanvasview.md)
  A view that captures Apple Pencil input and displays the rendered results in an iOS app.
- [PKDrawing](./pkdrawingreference.md)
  A data structure that contains the drawing information captured by a canvas view.
- [PKStroke](./pkstrokereference.md)
  A class that represents the paths, boundaries and other properties of a stroke drawn on a canvas.
- [PKStrokePath](./pkstrokepathreference.md)
  A class that captures the components of a stroke and provides methods to find and interpolate points along the stroke’s path.
- [PKInk](./pkinkreference.md)
  Provides a description of the creation and rendering of marks on a canvas.
- [PKStrokeRenderState](./pkstrokerenderstatereference.md)
  An object that captures the render-time state of a stroke, such as grain texture position.
- [PKConvertedBezierPoint](./pkconvertedbezierpointreference.md)
  An object that provides information about a B-spline control point converted from a Bézier path.
- [PKFloatRange](./pkfloatrange.md)
  A utility class that represents range components of a stroke.
- [PKInkTypeReed](./pkinktypereed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepointreference)*