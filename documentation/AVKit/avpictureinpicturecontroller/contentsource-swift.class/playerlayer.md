# playerLayer

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The presenting player layer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var playerLayer: AVPlayerLayer? { get }
```

```objc
@property (nonatomic, readonly, nullable) AVPlayerLayer * playerLayer;
```

## Discussion

This value is `nil` if the content source doesn’t represent a player layer.

## See Also

### Accessing the presentation layer
- [var sampleBufferDisplayLayer: AVSampleBufferDisplayLayer?](./samplebufferdisplaylayer.md)
  The presenting sample buffer display layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/playerlayer)*