# addRepresentation(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds the specified image representation object to the image.

**Availability**:
- macOS

## Declaration

```swift
func addRepresentation(_ imageRep: NSImageRep)
```

```objc
- (void) addRepresentation:(NSImageRep *) imageRep;
```

## Discussion

After invoking this method, you may need to explicitly set features of the new image representation, such as the size, number of colors, and so on. This is true particularly when the `NSImage` object has multiple image representations to choose from. See [`NSImageRep`](../nsimagerep.md) and its subclasses for the methods you use to complete initialization.

Any representation added by this method is retained by the receiver. Image representations cannot be shared among multiple `NSImage` objects.

## Parameters

- `imageRep`: The image representation to add.

## See Also

### Working with Representations of Images
- [func addRepresentations([NSImageRep])](./addrepresentations%28_%29.md)
  Adds an array of image representation objects to the image.
- [var representations: [NSImageRep]](./representations.md)
  An array containing all of the image object’s image representations.
- [func removeRepresentation(NSImageRep)](./removerepresentation%28_%29.md)
  Removes and releases the specified image representation.
- [func bestRepresentation(for: NSRect, context: NSGraphicsContext?, hints: [NSImageRep.HintKey : Any]?) -> NSImageRep?](./bestrepresentation%28for,context,hints%29.md)
  Returns the best representation of the image for the specified rectangle using the provided hints.
- [NSImageRep.HintKey](../nsimagerep/hintkey.md)
  Constants for the keys to include in a hints dictionary when drawing the image.
- [NSImage.LayoutDirection](./layoutdirection.md)
  Constants that describe the layout direction for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/addrepresentation(_:))*