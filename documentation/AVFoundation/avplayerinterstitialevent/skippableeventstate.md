# AVPlayerInterstitialEvent.SkippableEventState

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AVPlayerInterstitialEventSkippableEventState : NSInteger;
```

## Topics

### Event states
- [AVPlayerInterstitialEvent.SkippableEventState.eligible](./skippableeventstate/eligible.md)
  Indicates that the interstitial event is currently skippable.
- [AVPlayerInterstitialEvent.SkippableEventState.noLongerEligible](./skippableeventstate/nolongereligible.md)
  Indicates that the interstitial event is no longer eligible to be skipped.
- [AVPlayerInterstitialEvent.SkippableEventState.notSkippable](./skippableeventstate/notskippable.md)
  Indicates that the interstitial event is not skippable.
- [AVPlayerInterstitialEvent.SkippableEventState.notYetEligible](./skippableeventstate/notyeteligible.md)
  Indicates that the interstitial event will eventually become eligible to be skipped.
### Initializers
- [init?(rawValue: Int)](./skippableeventstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing skipping behavior
- [var skipControlLocalizedLabelBundleKey: String?](./skipcontrollocalizedlabelbundlekey.md)
  The key defined in the AVPlayerInterstitialEventController’s localizedStringsBundle that points to the localized label for the skip button.
- [var skipControlTimeRange: CMTimeRange](./skipcontroltimerange.md)
  The time range within the duration of the interstitial event for which a skip button should be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/skippableeventstate)*