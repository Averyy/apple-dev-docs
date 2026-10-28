# PKStrokeRenderStateReference

**Framework**: PencilKit  
**Kind**: class  
**Role**: Class

An object that captures the render-time state of a stroke, such as grain texture position.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
class PKStrokeRenderStateReference
```

```objc
@interface PKStrokeRenderState : NSObject
```

## Overview

`PKStrokeRenderState` is the Objective-C representation of a stroke’s rendering context. It conforms to `NSCopying` and `NSSecureCoding` for archiving. In Swift, use the equivalent value type [`PKStroke.RenderState`](./pkstroke-swift.struct/renderstate-swift.struct.md) instead.

## Topics

### Getting the render state
- [var grainOffset: CGPoint](./pkstrokerenderstatereference/grainoffset.md)
  The pre-transform position of the grain texture for strokes with a backing grain texture such as crayon.
### Using Swift types
- [PKStroke.RenderState](./pkstroke-swift.struct/renderstate-swift.struct.md)
  A value that captures the render-time state of a stroke, such as grain texture position.
### Initializers
- [convenience init(PKStroke.RenderState)](./pkstrokerenderstatereference/init%28_%29.md)
  Creates a `PKStrokeRenderStateReference` from its Swift counterpart `PKStroke.RenderState`.
- [init?(coder: NSCoder)](./pkstrokerenderstatereference/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

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
- [PKConvertedBezierPoint](./pkconvertedbezierpointreference.md)
  An object that provides information about a B-spline control point converted from a Bézier path.
- [PKFloatRange](./pkfloatrange.md)
  A utility class that represents range components of a stroke.
- [PKInkTypeReed](./pkinktypereed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokerenderstatereference)*