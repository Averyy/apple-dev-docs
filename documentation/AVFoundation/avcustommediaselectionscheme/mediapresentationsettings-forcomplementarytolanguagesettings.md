# mediaPresentationSettings(for:complementaryToLanguage:settings:)

**Framework**: AVFoundation  
**Kind**: method

Provides an array of media presentation settings that can be effective at the same time as the specified language and settings for other selectors of the receiver.

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
func mediaPresentationSettings(for selector: AVMediaPresentationSelector, complementaryToLanguage language: String?, settings: [AVMediaPresentationSetting]) -> [AVMediaPresentationSetting]
```

#### Discussion

If the content is authored to provide a collection of AVMediaSelectionOptions that include one or more with all of the combinations of media characteristics of the specified AVMediaPresentationSettings together with all of the settings of the specified AVMediaPresentationSelector, this method will return all of the settings for that selector. However, if one or more of the available combinations are not possessed by any of the AVMediaSelectionOptions, it will return fewer.

## Parameters

- `selector`: The AVMediaPresentationSelector for which complementary settings are requested.
- `language`: A BCP 47 language tag chosen among the availableLanguages of the receiver. If no language setting pertains, can be nil.
- `settings`: A collection of AVMediaPresentationSettings provided by selectors of the receiver other than the specified selector. Because no two AVMediaPresentationSettings of the same AVMediaPresentationSelector are complementary, an empty array will be returned if you specify more than one setting for any selector.

## See Also

- [var availableLanguages: [String]](avcustommediaselectionscheme/availablelanguages.md)
  Provides available language choices.
- [var selectors: [AVMediaPresentationSelector]](avcustommediaselectionscheme/selectors.md)
  Provides custom settings.
- [var shouldOfferLanguageSelection: Bool](avcustommediaselectionscheme/shouldofferlanguageselection.md)
  Indicates whether an alternative selection interface should provide a menu of language choices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcustommediaselectionscheme/mediapresentationsettings(for:complementarytolanguage:settings:))*