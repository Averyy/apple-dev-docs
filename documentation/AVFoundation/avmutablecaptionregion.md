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
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class AVCaptionRegion](avcaptionregion.md)
  An object that represents the region in which the system presents a caption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecaptionregion)*