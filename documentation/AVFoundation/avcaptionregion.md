# AVCaptionRegion

**Framework**: AVFoundation  
**Kind**: class

An object that represents the region in which the system presents a caption.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class AVCaptionRegion
```

#### Overview

The framework defines four regions, and doesn’t support configuring region settings.

## Topics

### Accessing Defined Regions
- [class var appleITTTop: AVCaptionRegion](avcaptionregion/appleitttop.md)
  The top region for iTT format captions.
- [class var appleITTBottom: AVCaptionRegion](avcaptionregion/appleittbottom.md)
  The bottom region for iTT format captions.
- [class var appleITTLeft: AVCaptionRegion](avcaptionregion/appleittleft.md)
  The left region for iTT format captions.
- [class var appleITTRight: AVCaptionRegion](avcaptionregion/appleittright.md)
  The right region for iTT format captions.
- [class var subRipTextBottom: AVCaptionRegion](avcaptionregion/subriptextbottom.md)
  The bottom caption region for SubRip Text (SRT) format captions.
### Identifying a Region
- [var identifier: String?](avcaptionregion/identifier.md)
  A string that identifies the region.
### Accessing Dimensions
- [struct AVCaptionDimension](avcaptiondimension.md)
  A structure that defines a caption dimension.
### Accessing the Location
- [var origin: AVCaptionPoint](avcaptionregion/origin.md)
  The region’s top-left position.
- [struct AVCaptionPoint](avcaptionpoint.md)
  A structure that defines the origin point for a caption.
### Accessing the Size
- [var size: AVCaptionSize](avcaptionregion/size.md)
  The height and width of the region.
- [struct AVCaptionSize](avcaptionsize.md)
  A structure that defines the height and width of a caption.
### Accessing the Display Alignment
- [var displayAlignment: AVCaptionRegion.DisplayAlignment](avcaptionregion/displayalignment-swift.property.md)
  The alignment of lines for the region.
- [AVCaptionRegion.DisplayAlignment](avcaptionregion/displayalignment-swift.enum.md)
  Constants that indicate the alignment of lines in a region.
### Accessing the Scroll Mode
- [var scroll: AVCaptionRegion.Scroll](avcaptionregion/scroll-swift.property.md)
  The scroll mode of the region.
- [AVCaptionRegion.Scroll](avcaptionregion/scroll-swift.enum.md)
  Constants that indicate the scrolling effects the system applies to a region.
### Accessing the Writing Mode
- [var writingMode: AVCaptionRegion.WritingMode](avcaptionregion/writingmode-swift.property.md)
  The block and inline progression direction of the region.
- [AVCaptionRegion.WritingMode](avcaptionregion/writingmode-swift.enum.md)
  Constants that indicate the writing mode for a region.
### Processing Regions
- [func mutableCopy(with: NSZone?) -> Any](avcaptionregion/mutablecopy(with:).md)
  Creates a mutable copy of a caption region.
- [func encode(with: NSCoder)](avcaptionregion/encode(with:).md)
  Encodes the region using the specified encoder.
- [func isEqual(Any) -> Bool](avcaptionregion/isequal(_:).md)
  Returns a Boolean value that indicates whether an object equals another.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVMutableCaptionRegion](avmutablecaptionregion.md)
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

- [class AVMutableCaptionRegion](avmutablecaptionregion.md)
  A mutable caption region subclass that you use to create new caption regions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionregion)*