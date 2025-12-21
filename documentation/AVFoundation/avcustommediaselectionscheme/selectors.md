# selectors

**Framework**: AVFoundation  
**Kind**: property

Provides custom settings.

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
var selectors: [AVMediaPresentationSelector] { get }
```

## See Also

- [var availableLanguages: [String]](avcustommediaselectionscheme/availablelanguages.md)
  Provides available language choices.
- [var shouldOfferLanguageSelection: Bool](avcustommediaselectionscheme/shouldofferlanguageselection.md)
  Indicates whether an alternative selection interface should provide a menu of language choices.
- [func mediaPresentationSettings(for: AVMediaPresentationSelector, complementaryToLanguage: String?, settings: [AVMediaPresentationSetting]) -> [AVMediaPresentationSetting]](avcustommediaselectionscheme/mediapresentationsettings(for:complementarytolanguage:settings:).md)
  Provides an array of media presentation settings that can be effective at the same time as the specified language and settings for other selectors of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcustommediaselectionscheme/selectors)*