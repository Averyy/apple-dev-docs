# PKConvertedBezierPointReference

**Framework**: PencilKit  
**Kind**: class  
**Role**: Class

An object that provides information about a B-spline control point converted from a Bézier path.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
class PKConvertedBezierPointReference
```

```objc
@interface PKConvertedBezierPoint : NSObject
```

## Overview

`PKConvertedBezierPointReference` is passed to the `pointProvider` block of `PKStrokePathReference/initWithBezierPath:creationDate:pointProvider:` so you can initialize each `PKStrokePoint` of the resulting path with appropriate values. A single instance is reused for each point in the conversion.

In Swift, use the equivalent value type [`PKStrokePath.ConvertedBezierPoint`](./pkstrokepath-swift.struct/convertedbezierpoint.md) instead.

## Topics

### Getting the point data
- [var index: Int](./pkconvertedbezierpointreference/index.md)
  The index of the point along the path.
- [var pointCount: Int](./pkconvertedbezierpointreference/pointcount.md)
  The total number of B-Spline control points in the path.
- [var location: CGPoint](./pkconvertedbezierpointreference/location.md)
  The location of the cubic uniform B-Spline control point.
- [var bezierSegmentIndex: Int](./pkconvertedbezierpointreference/beziersegmentindex.md)
  The index of the Bézier segment the point originates from, not including `move to` elements.
### Using Swift types
- [PKStrokePath.ConvertedBezierPoint](./pkstrokepath-swift.struct/convertedbezierpoint.md)
  Information about a B-spline control point converted from a Bézier path.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

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
- [PKStrokePoint](./pkstrokepointreference.md)
  A class that represents the properties of a specific point along a stroke’s path.
- [PKInk](./pkinkreference.md)
  Provides a description of the creation and rendering of marks on a canvas.
- [PKStrokeRenderState](./pkstrokerenderstatereference.md)
  An object that captures the render-time state of a stroke, such as grain texture position.
- [PKFloatRange](./pkfloatrange.md)
  A utility class that represents range components of a stroke.
- [PKInkTypeReed](./pkinktypereed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkconvertedbezierpointreference)*