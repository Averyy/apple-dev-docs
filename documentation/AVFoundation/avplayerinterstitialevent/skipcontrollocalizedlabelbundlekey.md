# skipControlLocalizedLabelBundleKey

**Framework**: AVFoundation  
**Kind**: property

The key defined in the AVPlayerInterstitialEventController’s localizedStringsBundle that points to the localized label for the skip button.

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
var skipControlLocalizedLabelBundleKey: String? { get set }
```

#### Discussion

If the value of the property is nil, the skip button may contain a generic label depending on the implementation of the UI that’s in use. To ensure the best available user experience in various playback configurations, including external playback, set a value for this property that provides localized translations of skip control labels.

## See Also

- [var skipControlTimeRange: CMTimeRange](avplayerinterstitialevent/skipcontroltimerange.md)
  The time range within the duration of the interstitial event for which a skip button should be displayed.
- [AVPlayerInterstitialEvent.SkippableEventState](avplayerinterstitialevent/skippableeventstate.md)
  These constants describe the state for a skippable AVPlayerInterstitialEvent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/skipcontrollocalizedlabelbundlekey)*