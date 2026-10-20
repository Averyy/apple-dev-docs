# MPNowPlayingInfoLanguageOption

**Framework**: Media Player  
**Kind**: class  
**Role**: Class

A set of interfaces for setting the language option for the Now Playing item.

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
class MPNowPlayingInfoLanguageOption
```

```objc
@interface MPNowPlayingInfoLanguageOption : NSObject
```

#### Overview

The [`MPNowPlayingInfoLanguageOption`](./mpnowplayinginfolanguageoption.md) and [`MPNowPlayingInfoLanguageOptionGroup`](./mpnowplayinginfolanguageoptiongroup.md) classes provide interfaces for setting information about language options, for example, audio and subtitles, in the Now Playing information area.

## Topics

### Creating a new language option
- [init(type: MPNowPlayingInfoLanguageOptionType, languageTag: String, characteristics: [String]?, displayName: String, identifier: String)](./mpnowplayinginfolanguageoption/init%28type,languagetag,characteristics,displayname,identifier%29.md)
  Creates a single language option.
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
- [enum MPNowPlayingInfoLanguageOptionType](./mpnowplayinginfolanguageoptiontype.md)
  The language option type to use for the Now Playing item.
### Retrieving a language option based on system preferences
- [func isAutomaticAudibleLanguageOption() -> Bool](./mpnowplayinginfolanguageoption/isautomaticaudiblelanguageoption%28%29.md)
  Returns a Boolean value that determines whether to use the best audible language option based on the system preferences.
- [func isAutomaticLegibleLanguageOption() -> Bool](./mpnowplayinginfolanguageoption/isautomaticlegiblelanguageoption%28%29.md)
  Returns a Boolean value that determines whether to use the best legible language option based on the system preferences.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Now Playing information
- [Becoming a now playable app](./becoming-a-now-playable-app.md)
  Ensure your app is eligible to become the Now Playing app by adopting best practices for providing Now Playing info and registering for remote command center actions.
- [class MPNowPlayingSession](./mpnowplayingsession.md)
  An object that manages Now Playing information and remote commands for multiple players.
- [class MPNowPlayingInfoCenter](./mpnowplayinginfocenter.md)
  An object for setting the Now Playing information for media that your app plays.
- [class MPNowPlayingInfoLanguageOptionGroup](./mpnowplayinginfolanguageoptiongroup.md)
  A grouped set of language options where only a single language option can be active at a time.
- [Language option characteristic constants](./language-option-characteristic-constants.md)
  The constants for defining language characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoption)*