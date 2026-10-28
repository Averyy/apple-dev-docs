# languageOption

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The requested language option to change.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var languageOption: MPNowPlayingInfoLanguageOption { get }
```

```objc
@property (nonatomic, readonly) MPNowPlayingInfoLanguageOption * languageOption;
```

## Discussion

The supplied language option may be the Automatic Legible Language Option, which requests the best legible language based on the user’s preferences. See [`isAutomaticLegibleLanguageOption()`](../mpnowplayinginfolanguageoption/isautomaticlegiblelanguageoption%28%29.md).

## See Also

### Changing the language option
- [var setting: MPChangeLanguageOptionSetting](./setting.md)
  The extent of the language setting change.
- [enum MPChangeLanguageOptionSetting](../mpchangelanguageoptionsetting.md)
  The states that determine when language option changes take effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpchangelanguageoptioncommandevent/languageoption)*