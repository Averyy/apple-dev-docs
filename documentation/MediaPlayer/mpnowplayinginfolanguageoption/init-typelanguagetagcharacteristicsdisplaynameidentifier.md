# init(type:languageTag:characteristics:displayName:identifier:)

**Framework**: Media Player  
**Kind**: init

Creates a single language option.

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
init(type languageOptionType: MPNowPlayingInfoLanguageOptionType, languageTag: String, characteristics languageOptionCharacteristics: [String]?, displayName: String, identifier: String)
```

#### Return Value

A newly created language option containing the passed characteristics.

## Parameters

- `languageOptionType`: The type, audio or legible, for the language option.
- `languageTag`: The IETF BCP 47 language tag for the language option.
- `languageOptionCharacteristics`: An array of characteristics that describes the language option.
- `displayName`: The name for displaying the language option.
- `identifier`: A unique identifier for the language option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoption/init(type:languagetag:characteristics:displayname:identifier:))*