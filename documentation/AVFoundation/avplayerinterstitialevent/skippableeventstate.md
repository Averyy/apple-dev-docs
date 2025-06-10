# AVPlayerInterstitialEvent.SkippableEventState

**Framework**: AVFoundation  
**Kind**: enum

These constants describe the state for a skippable AVPlayerInterstitialEvent.

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
enum SkippableEventState
```

## Topics

### Enumeration Cases
- [AVPlayerInterstitialEvent.SkippableEventState.eligible](avplayerinterstitialevent/skippableeventstate/eligible.md)
  Indicates that the interstitial event is currently skippable.
- [AVPlayerInterstitialEvent.SkippableEventState.noLongerEligible](avplayerinterstitialevent/skippableeventstate/nolongereligible.md)
  Indicates that the interstitial event is no longer eligible to be skipped.
- [AVPlayerInterstitialEvent.SkippableEventState.notSkippable](avplayerinterstitialevent/skippableeventstate/notskippable.md)
  Indicates that the interstitial event is not skippable.
- [AVPlayerInterstitialEvent.SkippableEventState.notYetEligible](avplayerinterstitialevent/skippableeventstate/notyeteligible.md)
  Indicates that the interstitial event will eventually become eligible to be skipped.
### Initializers
- [init?(rawValue: Int)](avplayerinterstitialevent/skippableeventstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/skippableeventstate)*