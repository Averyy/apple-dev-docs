# languageTag

**Framework**: Media Player  
**Kind**: property

The abbreviated language code for the language option.

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
var languageTag: String? { get }
```

#### Discussion

This property contains the IETF BCP 47 language code for the language option. A value of [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) indicates that this option is disabled.

## See Also

- [var displayName: String?](mpnowplayinginfolanguageoption/displayname.md)
  The display name for a language option.
- [var identifier: String?](mpnowplayinginfolanguageoption/identifier.md)
  The unique identifier for the language option.
- [var languageOptionCharacteristics: [String]?](mpnowplayinginfolanguageoption/languageoptioncharacteristics.md)
  The characteristics that describe the content of the language option.
- [var languageOptionType: MPNowPlayingInfoLanguageOptionType](mpnowplayinginfolanguageoption/languageoptiontype.md)
  The type of language option.
- [enum MPNowPlayingInfoLanguageOptionType](mpnowplayinginfolanguageoptiontype.md)
  The language option type to use for the Now Playing item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoption/languagetag)*