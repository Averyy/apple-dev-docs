# allowsCaptureOfClearKeyVideo

**Framework**: AVFoundation  
**Kind**: property

Indicates whether the video output of ClearKey Encrypted Video can be captured

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
nonisolated
var allowsCaptureOfClearKeyVideo: Bool { get set }
```

#### Discussion

When set to YES, and the video being played by AVPlayer is Clear Key encrypted, allows video to be captured in screenshots and screen recordings, and via APIs like AVPlayerItemVideoOutput and ScreenCaptureKit. When NO, Clear Key encrypted video will not be included in such captured video. This property has no effect on content protected by FairPlay Streaming. Default is NO.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/allowscaptureofclearkeyvideo)*