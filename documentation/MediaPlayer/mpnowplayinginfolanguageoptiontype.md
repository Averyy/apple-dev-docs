# MPNowPlayingInfoLanguageOptionType

**Framework**: Media Player  
**Kind**: enum  
**Role**: Enumeration

The language option type to use for the Now Playing item.

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
enum MPNowPlayingInfoLanguageOptionType
```

```c
enum MPNowPlayingInfoLanguageOptionType : NSUInteger;
```

## Topics

### Enumeration Cases
- [MPNowPlayingInfoLanguageOptionType.audible](./mpnowplayinginfolanguageoptiontype/audible.md)
  Indicates an audible language option is used.
- [MPNowPlayingInfoLanguageOptionType.legible](./mpnowplayinginfolanguageoptiontype/legible.md)
  Indicates a written language option is used.
### Initializers
- [init?(rawValue: UInt)](./mpnowplayinginfolanguageoptiontype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Retrieving language option properties
- [var displayName: String?](./mpnowplayinginfolanguageoption/displayname.md)
  The display name for a language option.
- [var identifier: String?](./mpnowplayinginfolanguageoption/identifier.md)
  The unique identifier for the language option.
- [var languageOptionCharacteristics: [String]?](./mpnowplayinginfolanguageoption/languageoptioncharacteristics.md)
  The characteristics that describe the content of the language option.
- [var languageTag: String?](./mpnowplayinginfolanguageoption/languagetag.md)
  The abbreviated language code for the language option.
- [var languageOptionType: MPNowPlayingInfoLanguageOptionType](./mpnowplayinginfolanguageoption/languageoptiontype.md)
  The type of language option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiontype)*