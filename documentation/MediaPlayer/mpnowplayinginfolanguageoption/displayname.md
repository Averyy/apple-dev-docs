# displayName

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The display name for a language option.

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
var displayName: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * displayName;
```

## See Also

### Retrieving language option properties
- [var identifier: String?](./identifier.md)
  The unique identifier for the language option.
- [var languageOptionCharacteristics: [String]?](./languageoptioncharacteristics.md)
  The characteristics that describe the content of the language option.
- [var languageTag: String?](./languagetag.md)
  The abbreviated language code for the language option.
- [var languageOptionType: MPNowPlayingInfoLanguageOptionType](./languageoptiontype.md)
  The type of language option.
- [enum MPNowPlayingInfoLanguageOptionType](../mpnowplayinginfolanguageoptiontype.md)
  The language option type to use for the Now Playing item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoption/displayname)*