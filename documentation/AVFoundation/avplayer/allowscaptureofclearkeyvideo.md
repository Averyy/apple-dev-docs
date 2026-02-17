# allowsCaptureOfClearKeyVideo

**Framework**: AVFoundation  
**Kind**: property

Indicates whether the video output of ClearKey Encrypted Video can be captured

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- tvOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)
- watchOS 26.4+ (Beta)

## Declaration

```swift
nonisolated
var allowsCaptureOfClearKeyVideo: Bool { get set }
```

#### Discussion

When set to YES, and the video being played by AVPlayer is Clear Key Encrypted, Video Output can be captured. This applies to user functionality like Screenshots as well as APIs like AVPlayerItemVideoOutput. If NO, any capture of the video output of any encrypted content is blacked out. This property has no effect on DRM protected content e.g. FairPlay / Pastis encrypted content. Default is NO


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/allowscaptureofclearkeyvideo)*