# NSImageRep.HintKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants for the keys to include in a hints dictionary when drawing the image.

**Availability**:
- macOS

## Declaration

```swift
struct HintKey
```

```c
typedef NSString * NSImageHintKey;
```

## Topics

### Hint Keys
- [static let ctm: NSImageRep.HintKey](./hintkey/ctm.md)
  A context transform hint.
- [static let interpolation: NSImageRep.HintKey](./hintkey/interpolation.md)
  An interpolation hint.
- [static let userInterfaceLayoutDirection: NSImageRep.HintKey](./hintkey/userinterfacelayoutdirection.md)
  A layout direction hint.
### Initializers
- [init(rawValue: String)](./hintkey/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Working with Representations of Images
- [func addRepresentation(NSImageRep)](../nsimage/addrepresentation%28_%29.md)
  Adds the specified image representation object to the image.
- [func addRepresentations([NSImageRep])](../nsimage/addrepresentations%28_%29.md)
  Adds an array of image representation objects to the image.
- [var representations: [NSImageRep]](../nsimage/representations.md)
  An array containing all of the image object’s image representations.
- [func removeRepresentation(NSImageRep)](../nsimage/removerepresentation%28_%29.md)
  Removes and releases the specified image representation.
- [func bestRepresentation(for: NSRect, context: NSGraphicsContext?, hints: [NSImageRep.HintKey : Any]?) -> NSImageRep?](../nsimage/bestrepresentation%28for,context,hints%29.md)
  Returns the best representation of the image for the specified rectangle using the provided hints.
- [NSImage.LayoutDirection](../nsimage/layoutdirection.md)
  Constants that describe the layout direction for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/hintkey)*