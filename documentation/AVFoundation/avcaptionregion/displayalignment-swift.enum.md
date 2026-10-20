# AVCaptionRegion.DisplayAlignment

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the alignment of lines in a region.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
enum DisplayAlignment
```

```c
enum AVCaptionRegionDisplayAlignment : NSInteger;
```

#### Overview

When you insert a caption line, the region places it relative to existing lines. The system determines the order in which the region places lines by its block progression direction. For example, English captions’ block progression direction are top-to-bottom, while Japanese vertical captions use right-to-left.

## Topics

### Display alignments
- [AVCaptionRegion.DisplayAlignment.before](./displayalignment-swift.enum/before.md)
  An alignment that positions lines at the top of the block progression direction.
- [AVCaptionRegion.DisplayAlignment.center](./displayalignment-swift.enum/center.md)
  An alignment that positions lines in the middle of the block progression direction.
- [AVCaptionRegion.DisplayAlignment.after](./displayalignment-swift.enum/after.md)
  An alignment that positions lines at the bottom of the block progression direction.
### Initializers
- [init?(rawValue: Int)](./displayalignment-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing the display alignment
- [var displayAlignment: AVCaptionRegion.DisplayAlignment](./displayalignment-swift.property.md)
  The alignment of lines for the region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionregion/displayalignment-swift.enum)*