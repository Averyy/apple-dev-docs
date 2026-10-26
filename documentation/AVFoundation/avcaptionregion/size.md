# size

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The height and width of the region.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var size: AVCaptionSize { get }
```

```objc
@property (nonatomic, readonly) AVCaptionSize size;
```

#### Discussion

CEA608 closed captions limit the [`height`](../avcaptionsize/height.md) property’s value to 1 cell, except when the value of its [`scroll`](./scroll-swift.property.md) property is [`AVCaptionRegion.Scroll.rollUp`](./scroll-swift.enum/rollup.md). In this case, the [`height`](../avcaptionsize/height.md) property’s value must be 2, 3 or 4 cells.

> **Note**:  The caption size has an unspecified height and width when the region doesn’t have width or height information.

## See Also

### Accessing the size
- [struct AVCaptionSize](../avcaptionsize.md)
  A structure that defines the height and width of a caption.
- [AVCaptionSizeMake](../avcaptionsizemake.md)
  Creates a caption size with the specified width and height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionregion/size)*