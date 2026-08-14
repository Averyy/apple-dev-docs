# AVMutableCaptionRegion

**Framework**: AVFoundation  
**Kind**: class

A mutable caption region subclass that you use to create new caption regions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class AVMutableCaptionRegion
```

## Topics

### Creating a caption region
- [init()](avmutablecaptionregion/init.md)
  Creates a caption region.
- [init(identifier: String)](avmutablecaptionregion/init(identifier:).md)
  Creates a caption region that has an identifier.
### Configuring the region
- [var origin: AVCaptionPoint](avmutablecaptionregion/origin.md)
  The region’s top-left position.
- [var size: AVCaptionSize](avmutablecaptionregion/size.md)
  The height and width of the region.
- [var displayAlignment: AVCaptionRegion.DisplayAlignment](avmutablecaptionregion/displayalignment.md)
  The alignment of lines for the region.
- [var scroll: AVCaptionRegion.Scroll](avmutablecaptionregion/scroll.md)
  The scroll mode of the region.
- [var writingMode: AVCaptionRegion.WritingMode](avmutablecaptionregion/writingmode.md)
  The block and inline progression direction of the region.

## Relationships

### Inherits From
- [AVCaptionRegion](avcaptionregion.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSMutableCopying](../foundation/nsmutablecopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class AVCaptionRegion](avcaptionregion.md)
  An object that represents the region in which the system presents a caption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecaptionregion)*