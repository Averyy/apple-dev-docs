# PKDrawingReference

**Framework**: PencilKit  
**Kind**: class

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

#### Overview

A [`PKDrawingReference`](pkdrawingreference.md) object stores the user-drawn content from a [`PKCanvasView`](pkcanvasview.md) object. You use drawing objects to store the data associated with your user’s drawings. You can save this data with the rest of your app’s content, and you can use that saved data to create a new drawing object later. You can also generate an image based on the drawn content.

## Topics

### Creating a drawing object
- [init(data: Data) throws](pkdrawingreference/init(data:).md)
  Creates a drawing object and populates it with previously drawn content.
- [convenience init(strokes: [PKStroke])](pkdrawingreference/init(strokes:).md)
  Creates a drawing object with the strokes you supply.
- [init()](pkdrawingreference/init.md)
  Creates an empty drawing object.
### Getting the canvas bounds
- [var bounds: CGRect](pkdrawingreference/bounds.md)
  The smallest rectangle used to represent the content’s bounds, taking into account line widths of that content.
### Generating an image
- [func image(from: CGRect, scale: CGFloat) -> UIImage](pkdrawingreference/image(from:scale:).md)
  Returns an image object that contains the specified portion of the drawing.
### Getting the drawing data
- [var strokes: [PKStroke]](pkdrawingreference/strokes.md)
  An array of strokes used to represent the drawing.
- [func dataRepresentation() -> Data](pkdrawingreference/datarepresentation.md)
  Returns a representation of the rendered content as data.
- [let PKAppleDrawingTypeIdentifier: CFString](pkappledrawingtypeidentifier.md)
  The uniform type identifier for data associated with a drawing object.
### Modifying the drawing
- [func applying(CGAffineTransform) -> PKDrawing](pkdrawingreference/applying(_:).md)
  Returns a new drawing object by applying the specified transform to a copy of the current object’s contents.
- [func appendingStrokes([PKStroke]) -> PKDrawing](pkdrawingreference/appendingstrokes(_:).md)
  Returns a copy of the current drawing with the strokes you provide appended.
- [func appending(PKDrawing) -> PKDrawing](pkdrawingreference/appending(_:).md)
  Returns a new drawing created by appending the current drawing with another drawing you provide.
### Supporting backward compatibility
- [var requiredContentVersion: PKContentVersion](pkdrawingreference/requiredcontentversion.md)
  The version of PencilKit necessary to use the drawing.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawingreference)*