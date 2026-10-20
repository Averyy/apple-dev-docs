# localizedStringsBundle

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The bundle that contains the localized strings to be used by the AVPlayerInterstitialEventController.

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
@NSCopying
var localizedStringsBundle: Bundle? { get set }
```

```objc
@property (copy, nullable) NSBundle * localizedStringsBundle;
```

#### Discussion

If the value of the property is nil, any UI elements triggered by the AVPlayerInterstitialEventController, such as the skip button, may contain a generic label based on the implementation of the UI that’s in use. To ensure the best available user experience in various playback configurations, including external playback, set a value for this property that provides localized translations of skip control labels.

## See Also

### Accessing strings
- [var localizedStringsTableName: String?](./localizedstringstablename.md)
  The name of the table in the bundle that contains the localized strings to be used by the AVPlayerInterstitialEventController.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventcontroller/localizedstringsbundle)*