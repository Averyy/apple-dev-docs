# currentEventSkippableState

**Framework**: AVFoundation  
**Kind**: property

The skippable event state for the currentEvent.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var currentEventSkippableState: AVPlayerInterstitialEvent.SkippableEventState { get }
```

#### Discussion

If currentEvent is nil, then the value will be AVPlayerInterstitialEventSkippableEventStateNotSkippable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/currenteventskippablestate)*