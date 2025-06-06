# NSImageRep.HintKey

**Framework**: AppKit  
**Kind**: struct

Constants for the keys to include in a hints dictionary when drawing the image.

**Availability**:
- macOS ?+

## Declaration

```swift
struct HintKey
```

## Topics

### Hint Keys
- [static let ctm: NSImageRep.HintKey](nsimagerep/hintkey/ctm.md)
  A context transform hint.
- [static let interpolation: NSImageRep.HintKey](nsimagerep/hintkey/interpolation.md)
  An interpolation hint.
- [static let userInterfaceLayoutDirection: NSImageRep.HintKey](nsimagerep/hintkey/userinterfacelayoutdirection.md)
  A layout direction hint.
### Initializers
- [init(rawValue: String)](nsimagerep/hintkey/init(rawvalue:).md)

## Relationships

### Conforms To
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
- [NSImage.LayoutDirection](nsimage/layoutdirection.md)
  Constants that describe the layout direction for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/hintkey)*