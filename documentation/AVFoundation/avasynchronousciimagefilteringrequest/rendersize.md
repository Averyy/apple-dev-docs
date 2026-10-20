# renderSize

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The width and height, in pixels, of the frame being processed.

**Availability**:
- iOS 9.0+ - Deprecated in 27.0
- iPadOS 9.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.11+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use AVCIImageFilteringParameters instead

## Declaration

```swift
var renderSize: CGSize { get }
```

```objc
@property (nonatomic, readonly) CGSize renderSize;
```

#### Discussion

You can use this property if you need to work with Core Image filters that apply transforms to the image.

## See Also

### Getting contextual information for filtering
- [var compositionTime: CMTime](./compositiontime.md)
  The time in the video composition corresponding to the frame being processed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/rendersize)*