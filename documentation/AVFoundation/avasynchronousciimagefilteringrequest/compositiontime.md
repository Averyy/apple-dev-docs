# compositionTime

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The time in the video composition corresponding to the frame being processed.

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
var compositionTime: CMTime { get }
```

```objc
@property (nonatomic, readonly) CMTime compositionTime;
```

#### Discussion

You can use this property to vary the parameters of a filter over time.

## See Also

### Getting contextual information for filtering
- [var renderSize: CGSize](./rendersize.md)
  The width and height, in pixels, of the frame being processed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/compositiontime)*