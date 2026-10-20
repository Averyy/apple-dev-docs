# sampleBufferDisplayLayer

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The presenting sample buffer display layer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var sampleBufferDisplayLayer: AVSampleBufferDisplayLayer? { get }
```

```objc
@property (nonatomic, readonly, nullable) AVSampleBufferDisplayLayer * sampleBufferDisplayLayer;
```

#### Discussion

This value is `nil` if the content source doesn’t represent a sample buffer display layer.

## See Also

### Accessing the presentation layer
- [var playerLayer: AVPlayerLayer?](./playerlayer.md)
  The presenting player layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/samplebufferdisplaylayer)*