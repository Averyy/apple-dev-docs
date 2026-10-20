# removeRepresentation(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes and releases the specified image representation.

**Availability**:
- macOS

## Declaration

```swift
func removeRepresentation(_ imageRep: NSImageRep)
```

```objc
- (void) removeRepresentation:(NSImageRep *) imageRep;
```

## Parameters

- `imageRep`: The image representation object you want to remove.

## See Also

### Working with Representations of Images
- [func addRepresentation(NSImageRep)](./addrepresentation%28_%29.md)
  Adds the specified image representation object to the image.
- [func addRepresentations([NSImageRep])](./addrepresentations%28_%29.md)
  Adds an array of image representation objects to the image.
- [var representations: [NSImageRep]](./representations.md)
  An array containing all of the image object’s image representations.
- [func bestRepresentation(for: NSRect, context: NSGraphicsContext?, hints: [NSImageRep.HintKey : Any]?) -> NSImageRep?](./bestrepresentation%28for,context,hints%29.md)
  Returns the best representation of the image for the specified rectangle using the provided hints.
- [NSImageRep.HintKey](../nsimagerep/hintkey.md)
  Constants for the keys to include in a hints dictionary when drawing the image.
- [NSImage.LayoutDirection](./layoutdirection.md)
  Constants that describe the layout direction for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/removerepresentation(_:))*