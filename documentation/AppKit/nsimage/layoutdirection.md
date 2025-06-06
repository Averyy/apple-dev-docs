# NSImage.LayoutDirection

**Framework**: AppKit  
**Kind**: enum

Constants that describe the layout direction for the image.

**Availability**:
- macOS 10.12+

## Declaration

```swift
enum LayoutDirection
```

## Topics

### Layout Directions
- [NSImage.LayoutDirection.unspecified](nsimage/layoutdirection/unspecified.md)
  An unspecified layout direction.
- [NSImage.LayoutDirection.leftToRight](nsimage/layoutdirection/lefttoright.md)
  A left-to-right layout direction.
- [NSImage.LayoutDirection.rightToLeft](nsimage/layoutdirection/righttoleft.md)
  A right-to-left layout direction.
### Initializers
- [init?(rawValue: Int)](nsimage/layoutdirection/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func addRepresentation(NSImageRep)](nsimage/addrepresentation(_:).md)
  Adds the specified image representation object to the image.
- [func addRepresentations([NSImageRep])](nsimage/addrepresentations(_:).md)
  Adds an array of image representation objects to the image.
- [var representations: [NSImageRep]](nsimage/representations.md)
  An array containing all of the image object’s image representations.
- [func removeRepresentation(NSImageRep)](nsimage/removerepresentation(_:).md)
  Removes and releases the specified image representation.
- [func bestRepresentation(for: NSRect, context: NSGraphicsContext?, hints: [NSImageRep.HintKey : Any]?) -> NSImageRep?](nsimage/bestrepresentation(for:context:hints:).md)
  Returns the best representation of the image for the specified rectangle using the provided hints.
- [NSImageRep.HintKey](nsimagerep/hintkey.md)
  Constants for the keys to include in a hints dictionary when drawing the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/layoutdirection)*