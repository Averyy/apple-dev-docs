# mediaPresentationSettings(for:complementaryToLanguage:settings:)

**Framework**: AVFoundation  
**Kind**: method

Provides an array of media presentation settings that can be effective at the same time as the specified language and settings for other selectors of the receiver.

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
func mediaPresentationSettings(for selector: AVMediaPresentationSelector, complementaryToLanguage language: String?, settings: [AVMediaPresentationSetting]) -> [AVMediaPresentationSetting]
```

#### Discussion

If the content is authored to provide a collection of AVMediaSelectionOptions that include one or more with all of the combinations of media characteristics of the specified AVMediaPresentationSettings together with all of the settings of the specified AVMediaPresentationSelector, this method will return all of the settings for that selector. However, if one or more of the available combinations are not possessed by any of the AVMediaSelectionOptions, it will return fewer.

## Parameters

- `selector`: The AVMediaPresentationSelector for which complementary settings are requested.
- `language`: A BCP 47 language tag chosen among the availableLanguages of the receiver. If no language setting pertains, can be nil.
- `settings`: A collection of AVMediaPresentationSettings provided by selectors of the receiver other than the specified selector. Because no two AVMediaPresentationSettings of the same AVMediaPresentationSelector are complementary, an empty array will be returned if you specify more than one setting for any selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcustommediaselectionscheme/mediapresentationsettings(for:complementarytolanguage:settings:))*