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


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawingreference)*