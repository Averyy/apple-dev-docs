# representations

**Framework**: AppKit  
**Kind**: property

An array containing all of the image object’s image representations.

**Availability**:
- macOS ?+

## Declaration

```swift
var representations: [NSImageRep] { get }
```

#### Discussion

This property can contain zero or more [`NSImageRep`](nsimagerep.md) objects.

## See Also

- [func addRepresentation(NSImageRep)](nsimage/addrepresentation(_:).md)
  Adds the specified image representation object to the image.
- [func addRepresentations([NSImageRep])](nsimage/addrepresentations(_:).md)
  Adds an array of image representation objects to the image.
- [func removeRepresentation(NSImageRep)](nsimage/removerepresentation(_:).md)
  Removes and releases the specified image representation.
- [func bestRepresentation(for: NSRect, context: NSGraphicsContext?, hints: [NSImageRep.HintKey : Any]?) -> NSImageRep?](nsimage/bestrepresentation(for:context:hints:).md)
  Returns the best representation of the image for the specified rectangle using the provided hints.
- [NSImageRep.HintKey](nsimagerep/hintkey.md)
  Constants for the keys to include in a hints dictionary when drawing the image.
- [NSImage.LayoutDirection](nsimage/layoutdirection.md)
  Constants that describe the layout direction for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/representations)*