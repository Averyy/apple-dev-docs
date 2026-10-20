# AVMutableCaptionRegion

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVMutableCaptionRegion : AVCaptionRegion
```

## Topics

### Creating a caption region
- [init()](./avmutablecaptionregion/init%28%29.md)
  Creates a caption region.
- [init(identifier: String)](./avmutablecaptionregion/init%28identifier%29.md)
  Creates a caption region that has an identifier.
### Configuring the region
- [var origin: AVCaptionPoint](./avmutablecaptionregion/origin.md)
  The region’s top-left position.
- [var size: AVCaptionSize](./avmutablecaptionregion/size.md)
  The height and width of the region.
- [var displayAlignment: AVCaptionRegion.DisplayAlignment](./avmutablecaptionregion/displayalignment.md)
  The alignment of lines for the region.
- [var scroll: AVCaptionRegion.Scroll](./avmutablecaptionregion/scroll.md)
  The scroll mode of the region.
- [var writingMode: AVCaptionRegion.WritingMode](./avmutablecaptionregion/writingmode.md)
  The block and inline progression direction of the region.

## Relationships

### Inherits From
- [AVCaptionRegion](./avcaptionregion.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSMutableCopying](../Foundation/nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Regions
- [class AVCaptionRegion](./avcaptionregion.md)
  An object that represents the region in which the system presents a caption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecaptionregion)*