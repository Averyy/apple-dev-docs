# representations

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array containing all of the image object’s image representations.

**Availability**:
- macOS

## Declaration

```swift
var representations: [NSImageRep] { get }
```

```objc
@property (copy, readonly) NSArray<NSImageRep *> * representations;
```

## Discussion

This property can contain zero or more [`NSImageRep`](../nsimagerep.md) objects.

## See Also

### Working with Representations of Images
- [func addRepresentation(NSImageRep)](./addrepresentation%28_%29.md)
  Adds the specified image representation object to the image.
- [func addRepresentations([NSImageRep])](./addrepresentations%28_%29.md)
  Adds an array of image representation objects to the image.
- [func removeRepresentation(NSImageRep)](./removerepresentation%28_%29.md)
  Removes and releases the specified image representation.
- [func bestRepresentation(for: NSRect, context: NSGraphicsContext?, hints: [NSImageRep.HintKey : Any]?) -> NSImageRep?](./bestrepresentation%28for,context,hints%29.md)
  Returns the best representation of the image for the specified rectangle using the provided hints.
- [NSImageRep.HintKey](../nsimagerep/hintkey.md)
  Constants for the keys to include in a hints dictionary when drawing the image.
- [NSImage.LayoutDirection](./layoutdirection.md)
  Constants that describe the layout direction for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/representations)*