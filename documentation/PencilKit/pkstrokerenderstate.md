# PKStrokeRenderState

**Framework**: PencilKit  
**Kind**: class

An object that captures the render-time state of a stroke, such as grain texture position.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@interface PKStrokeRenderState : NSObject
```

#### Overview

`PKStrokeRenderState` is the Objective-C representation of a stroke’s rendering context. It conforms to `NSCopying` and `NSSecureCoding` for archiving. In Swift, use the equivalent value type [`PKStroke.RenderState`](pkstroke-swift.struct/renderstate-swift.struct.md) instead.

## Topics

### Getting the render state
- [grainOffset](pkstrokerenderstate/grainoffset.md)
  The pre-transform position of the grain texture for strokes with a backing grain texture such as crayon.
### Using Swift types
- [PKStroke.RenderState](pkstroke-swift.struct/renderstate-swift.struct.md)
  A value that captures the render-time state of a stroke, such as grain texture position.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/NSCopying.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class PKCanvasView](pkcanvasview.md)
  A view that captures Apple Pencil input and displays the rendered results in an iOS app.
- [class PKDrawingReference](pkdrawingreference.md)
  A data structure that contains the drawing information captured by a canvas view.
- [class PKStrokeReference](pkstrokereference.md)
  A class that represents the paths, boundaries and other properties of a stroke drawn on a canvas.
- [class PKStrokePathReference](pkstrokepathreference.md)
  A class that captures the components of a stroke and provides methods to find and interpolate points along the stroke’s path.
- [class PKStrokePointReference](pkstrokepointreference.md)
  A class that represents the properties of a specific point along a stroke’s path.
- [class PKInkReference](pkinkreference.md)
  Provides a description of the creation and rendering of marks on a canvas.
- [class PKConvertedBezierPointReference](pkconvertedbezierpointreference.md)
  An object that provides information about a B-spline control point converted from a Bézier path.
- [PKFloatRange](pkfloatrange.md)
  A utility class that represents range components of a stroke.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokerenderstate)*