# PKStrokeReference

**Framework**: PencilKit  
**Kind**: class  
**Role**: Class

A class that represents the paths, boundaries and other properties of a stroke drawn on a canvas.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class PKStrokeReference
```

```objc
@interface PKStroke : NSObject
```

## Topics

### Creating a stroke object
- [init(ink: PKInk, strokePath: PKStrokePath, transform: CGAffineTransform, mask: UIBezierPath?)](./pkstrokereference/init%28ink,strokepath,transform,mask%29.md)
  Creates a stroke with the line properties, path, transform, and mask that you specify.
- [init(ink: PKInk, strokePath: PKStrokePath, transform: CGAffineTransform, mask: UIBezierPath?, randomSeed: UInt32)](./pkstrokereference/init%28ink,strokepath,transform,mask,randomseed%29.md)
  Creates a stroke with the line properties, path, transform, mask, and random seed that you specify.
### Getting the stroke properties
- [var ink: PKInk](./pkstrokereference/ink.md)
  The line properties used to render this stroke.
- [var mask: UIBezierPath?](./pkstrokereference/mask.md)
  The pretransform mask used to clip the rendering of the stroke.
- [var maskedPathRanges: [__PKFloatRange]](./pkstrokereference/maskedpathranges.md)
  The range of points in the stroke path reference that intersect the stroke’s mask.
- [var path: PKStrokePath](./pkstrokereference/path.md)
  The B-spline path that describes this stroke.
- [var renderBounds: CGRect](./pkstrokereference/renderbounds.md)
  The bounds of the rendered stroke, including the width and line properties of the stroke after applying the transform.
- [var transform: CGAffineTransform](./pkstrokereference/transform.md)
  The affine transform of the stroke after rendering.
- [var randomSeed: UInt32](./pkstrokereference/randomseed.md)
  An unsigned 32-bit integer to use as a random seed for drawing strokes that use randomized effects.
### Supporting backward compatibility
- [var requiredContentVersion: PKContentVersion](./pkstrokereference/requiredcontentversion.md)
  The version of PencilKit necessary to use the stroke.
### Initializers
- [init(ink: PKInk, strokePath: PKStrokePath, transform: CGAffineTransform, mask: UIBezierPath?, randomSeed: UInt32, strokeID: UUID, renderGroupID: UUID?, renderState: PKStrokeRenderStateReference?)](./pkstrokereference/init%28ink,strokepath,transform,mask,randomseed,strokeid,rendergroupid,renderstate%29.md)
### Instance Properties
- [var renderGroupID: UUID?](./pkstrokereference/rendergroupid.md)
  A UUID that groups strokes for wet-ink compositing with compatible inks such as marker.
- [var renderState: PKStrokeRenderStateReference?](./pkstrokereference/renderstate.md)
  The render details of the stroke, such as particle positioning. Uses default rendering when nil.
- [var strokeID: UUID](./pkstrokereference/strokeid.md)
  The unique identity of the stroke.
### Instance Methods
- [func substroke(with: __PKFloatRange) -> PKStroke](./pkstrokereference/substroke%28with%29.md)
  Returns a copy of the stroke containing the control points in the specified range.

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
- [PKStrokePath](./pkstrokepathreference.md)
  A class that captures the components of a stroke and provides methods to find and interpolate points along the stroke’s path.
- [PKStrokePoint](./pkstrokepointreference.md)
  A class that represents the properties of a specific point along a stroke’s path.
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

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokereference)*