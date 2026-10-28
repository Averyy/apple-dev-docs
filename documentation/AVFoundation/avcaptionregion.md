# AVCaptionRegion

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVCaptionRegion : NSObject
```

## Overview

The framework defines four regions, and doesn’t support configuring region settings.

## Topics

### Accessing defined regions
- [class var appleITTTop: AVCaptionRegion](./avcaptionregion/appleitttop.md)
  The top region for iTT format captions.
- [class var appleITTBottom: AVCaptionRegion](./avcaptionregion/appleittbottom.md)
  The bottom region for iTT format captions.
- [class var appleITTLeft: AVCaptionRegion](./avcaptionregion/appleittleft.md)
  The left region for iTT format captions.
- [class var appleITTRight: AVCaptionRegion](./avcaptionregion/appleittright.md)
  The right region for iTT format captions.
- [class var subRipTextBottom: AVCaptionRegion](./avcaptionregion/subriptextbottom.md)
  The bottom caption region for SubRip Text (SRT) format captions.
### Identifying a region
- [var identifier: String?](./avcaptionregion/identifier.md)
  A string that identifies the region.
### Accessing dimensions
- [struct AVCaptionDimension](./avcaptiondimension.md)
  A structure that defines a caption dimension.
- [AVCaptionDimensionMake](./avcaptiondimensionmake.md)
  Creates a caption dimension with a value and unit type.
### Accessing the location
- [var origin: AVCaptionPoint](./avcaptionregion/origin.md)
  The region’s top-left position.
- [struct AVCaptionPoint](./avcaptionpoint.md)
  A structure that defines the origin point for a caption.
- [AVCaptionPointMake](./avcaptionpointmake.md)
  Creates a caption point with the specified x and y positions.
### Accessing the size
- [var size: AVCaptionSize](./avcaptionregion/size.md)
  The height and width of the region.
- [struct AVCaptionSize](./avcaptionsize.md)
  A structure that defines the height and width of a caption.
- [AVCaptionSizeMake](./avcaptionsizemake.md)
  Creates a caption size with the specified width and height.
### Accessing the display alignment
- [var displayAlignment: AVCaptionRegion.DisplayAlignment](./avcaptionregion/displayalignment-swift.property.md)
  The alignment of lines for the region.
- [AVCaptionRegion.DisplayAlignment](./avcaptionregion/displayalignment-swift.enum.md)
  Constants that indicate the alignment of lines in a region.
### Accessing the scroll mode
- [var scroll: AVCaptionRegion.Scroll](./avcaptionregion/scroll-swift.property.md)
  The scroll mode of the region.
- [AVCaptionRegion.Scroll](./avcaptionregion/scroll-swift.enum.md)
  Constants that indicate the scrolling effects the system applies to a region.
### Accessing the writing mode
- [var writingMode: AVCaptionRegion.WritingMode](./avcaptionregion/writingmode-swift.property.md)
  The block and inline progression direction of the region.
- [AVCaptionRegion.WritingMode](./avcaptionregion/writingmode-swift.enum.md)
  Constants that indicate the writing mode for a region.
### Processing regions
- [func mutableCopy(with: NSZone?) -> Any](./avcaptionregion/mutablecopy%28with%29.md)
  Creates a mutable copy of a caption region.
- [func encode(with: NSCoder)](./avcaptionregion/encode%28with%29.md)
  Encodes the region using the specified encoder.
- [func isEqual(Any) -> Bool](./avcaptionregion/isequal%28_%29.md)
  Returns a Boolean value that indicates whether an object equals another.
### Initializers
- [init?(coder: NSCoder)](./avcaptionregion/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [AVMutableCaptionRegion](./avmutablecaptionregion.md)
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
- [class AVMutableCaptionRegion](./avmutablecaptionregion.md)
  A mutable caption region subclass that you use to create new caption regions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionregion)*