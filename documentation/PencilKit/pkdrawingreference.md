# PKDrawingReference

**Framework**: PencilKit  
**Kind**: class  
**Role**: Class

A data structure that contains the drawing information captured by a canvas view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class PKDrawingReference
```

```objc
@interface PKDrawing : NSObject
```

#### Overview

A [`PKDrawingReference`](./pkdrawingreference.md) object stores the user-drawn content from a [`PKCanvasView`](./pkcanvasview.md) object. You use drawing objects to store the data associated with your user’s drawings. You can save this data with the rest of your app’s content, and you can use that saved data to create a new drawing object later. You can also generate an image based on the drawn content.

## Topics

### Creating a drawing object
- [init(data: Data) throws](./pkdrawingreference/init%28data%29.md)
  Creates a drawing object and populates it with previously drawn content.
- [convenience init(strokes: [PKStroke])](./pkdrawingreference/init%28strokes%29.md)
  Creates a drawing object with the strokes you supply.
- [init()](./pkdrawingreference/init%28%29.md)
  Creates an empty drawing object.
### Getting the canvas bounds
- [var bounds: CGRect](./pkdrawingreference/bounds.md)
  The smallest rectangle used to represent the content’s bounds, taking into account line widths of that content.
### Generating an image
- [func image(from: CGRect, scale: CGFloat) -> UIImage](./pkdrawingreference/image%28from,scale%29.md)
  Returns an image object that contains the specified portion of the drawing.
### Getting the drawing data
- [var strokes: [PKStroke]](./pkdrawingreference/strokes.md)
  An array of strokes used to represent the drawing.
- [func dataRepresentation() -> Data](./pkdrawingreference/datarepresentation%28%29.md)
  Returns a representation of the rendered content as data.
- [let PKAppleDrawingTypeIdentifier: CFString](./pkappledrawingtypeidentifier.md)
  The uniform type identifier for data associated with a drawing object.
### Modifying the drawing
- [func applying(CGAffineTransform) -> PKDrawing](./pkdrawingreference/applying%28_%29.md)
  Returns a new drawing object by applying the specified transform to a copy of the current object’s contents.
- [func appendingStrokes([PKStroke]) -> PKDrawing](./pkdrawingreference/appendingstrokes%28_%29.md)
  Returns a copy of the current drawing with the strokes you provide appended.
- [func appending(PKDrawing) -> PKDrawing](./pkdrawingreference/appending%28_%29.md)
  Returns a new drawing created by appending the current drawing with another drawing you provide.
### Supporting backward compatibility
- [var requiredContentVersion: PKContentVersion](./pkdrawingreference/requiredcontentversion.md)
  The version of PencilKit necessary to use the drawing.
### Initializers
- [init?(coder: NSCoder)](./pkdrawingreference/init%28coder%29.md)
### Instance Methods
- [func erasingStrokePath(PKStrokePath, mask: UIBezierPath?, transform: CGAffineTransform) -> PKDrawing](./pkdrawingreference/erasingstrokepath%28_,mask,transform%29.md)

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
- [PKConvertedBezierPoint](./pkconvertedbezierpointreference.md)
  An object that provides information about a B-spline control point converted from a Bézier path.
- [PKFloatRange](./pkfloatrange.md)
  A utility class that represents range components of a stroke.
- [PKInkTypeReed](./pkinktypereed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawingreference)*