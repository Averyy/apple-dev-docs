# currentEventSkipControlLabel

**Framework**: AVFoundation  
**Kind**: property

The skip control label for the currentEvent.

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
var currentEventSkipControlLabel: String? { get }
```

#### Discussion

If a localizedStringsBundle has been set on the AVPlayerInterstitialEventController, and a skipControlLocalizedLabelBundleKey is set on the currentEvent, then this value will be the localized string that was matched to the event’s skipControlLocalizedLabelBundleKey for the corresponding system language in the supplied Bundle, if any. If currentEvent is nil, then the value will be nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/currenteventskipcontrollabel)*