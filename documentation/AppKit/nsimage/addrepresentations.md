# addRepresentations(_:)

**Framework**: AppKit  
**Kind**: method

Adds an array of image representation objects to the image.

**Availability**:
- macOS ?+

## Declaration

```swift
func addRepresentations(_ imageReps: [NSImageRep])
```

#### Discussion

After invoking this method, you may need to explicitly set features of the new image representations, such as their size, number of colors, and so on. This is true particularly when the `NSImage` object has multiple image representations to choose from. See [`NSImageRep`](nsimagerep.md) and its subclasses for the methods you use to complete initialization.

Representations added by this method are retained by the receiver. Image representations cannot be shared among multiple `NSImage` objects.

## Parameters

- `imageReps`: An array of   objects.

## See Also

- [func addRepresentation(NSImageRep)](nsimage/addrepresentation(_:).md)
  Adds the specified image representation object to the image.
- [var representations: [NSImageRep]](nsimage/representations.md)
  An array containing all of the image object’s image representations.
- [func removeRepresentation(NSImageRep)](nsimage/removerepresentation(_:).md)
  Removes and releases the specified image representation.
- [func bestRepresentation(for: NSRect, context: NSGraphicsContext?, hints: [NSImageRep.HintKey : Any]?) -> NSImageRep?](nsimage/bestrepresentation(for:context:hints:).md)
  Returns the best representation of the image for the specified rectangle using the provided hints.
- [NSImageRep.HintKey](nsimagerep/hintkey.md)
  Constants for the keys to include in a hints dictionary when drawing the image.
- [NSImage.LayoutDirection](nsimage/layoutdirection.md)
  Constants that describe the layout direction for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/addrepresentations(_:))*