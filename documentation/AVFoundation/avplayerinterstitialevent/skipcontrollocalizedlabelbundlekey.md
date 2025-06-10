# skipControlLocalizedLabelBundleKey

**Framework**: AVFoundation  
**Kind**: property

The key defined in the AVPlayerInterstitialEventController’s localizedStringsBundle that points to the localized label for the skip button.

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
var skipControlLocalizedLabelBundleKey: String? { get set }
```

#### Discussion

If the value of the property is nil, the skip button may contain a generic label depending on the implementation of the UI that’s in use. To ensure the best available user experience in various playback configurations, including external playback, set a value for this property that provides localized translations of skip control labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/skipcontrollocalizedlabelbundlekey)*