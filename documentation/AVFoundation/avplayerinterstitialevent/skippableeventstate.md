# AVPlayerInterstitialEvent.SkippableEventState

**Framework**: AVFoundation  
**Kind**: enum

These constants describe the state for a skippable AVPlayerInterstitialEvent.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
enum SkippableEventState
```

## Topics

### Event states
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
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var skipControlLocalizedLabelBundleKey: String?](avplayerinterstitialevent/skipcontrollocalizedlabelbundlekey.md)
  The key defined in the AVPlayerInterstitialEventController’s localizedStringsBundle that points to the localized label for the skip button.
- [var skipControlTimeRange: CMTimeRange](avplayerinterstitialevent/skipcontroltimerange.md)
  The time range within the duration of the interstitial event for which a skip button should be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/skippableeventstate)*