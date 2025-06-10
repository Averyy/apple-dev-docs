# AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeSkipControlLabelKey

**Framework**: AVFoundation  
**Kind**: var

The dictionary key for the skip label of the event in the payload of the AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeNotification.

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
let AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeSkipControlLabelKey: String
```

#### Discussion

The value corresponding to this key is an NSString that’s the localized skip label if a localizedStringsBundle is set on the AVPlayerInterstitialEventController and a skipControlLocalizedLabelBundleKey on the AVPlayerInterstitialEvent whose skippable event state changed. Note that this key will not be present if there is no localizedStringsBundle set, or if the currentEventSkippableState changed to AVPlayerInterstitialEventSkippableEventStateNotSkippable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitorcurrenteventskippablestatedidchangeskipcontrollabelkey)*