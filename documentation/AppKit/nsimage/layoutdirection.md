# NSImage.LayoutDirection

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the layout direction for the image.

**Availability**:
- macOS 10.12+

## Declaration

```swift
enum LayoutDirection
```

```c
enum NSImageLayoutDirection : NSInteger;
```

## Topics

### Layout Directions
- [NSImage.LayoutDirection.unspecified](./layoutdirection/unspecified.md)
  An unspecified layout direction.
- [NSImage.LayoutDirection.leftToRight](./layoutdirection/lefttoright.md)
  A left-to-right layout direction.
- [NSImage.LayoutDirection.rightToLeft](./layoutdirection/righttoleft.md)
  A right-to-left layout direction.
### Initializers
- [init?(rawValue: Int)](./layoutdirection/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Working with Representations of Images
- [func addRepresentation(NSImageRep)](./addrepresentation%28_%29.md)
  Adds the specified image representation object to the image.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/layoutdirection)*