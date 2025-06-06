# MPNowPlayingInfoLanguageOptionGroup

**Framework**: Media Player  
**Kind**: class

A grouped set of language options where only a single language option can be active at a time.

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
class MPNowPlayingInfoLanguageOptionGroup
```

#### Overview

The `MPNowPlayingInfoLanguageOptionGroup` and [`MPNowPlayingInfoLanguageOption`](mpnowplayinginfolanguageoption.md) classes provide interfaces for setting information about language options, for example, audio and subtitles, in the Now Playing information area.

## Topics

### Creating a new language option group
- [init(languageOptions: [MPNowPlayingInfoLanguageOption], defaultLanguageOption: MPNowPlayingInfoLanguageOption?, allowEmptySelection: Bool)](mpnowplayinginfolanguageoptiongroup/init(languageoptions:defaultlanguageoption:allowemptyselection:).md)
  Creates a new language option group with the supplied language options.
### Retrieving language option group information
- [var allowEmptySelection: Bool](mpnowplayinginfolanguageoptiongroup/allowemptyselection.md)
  A Boolean that indicates whether the system requires a selection for the language option group.
- [var defaultLanguageOption: MPNowPlayingInfoLanguageOption?](mpnowplayinginfolanguageoptiongroup/defaultlanguageoption.md)
  The default language option for the group.
- [var languageOptions: [MPNowPlayingInfoLanguageOption]](mpnowplayinginfolanguageoptiongroup/languageoptions.md)
  The available language options for the group.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Becoming a now playable app](becoming-a-now-playable-app.md)
  Ensure your app is eligible to become the Now Playing app by adopting best practices for providing Now Playing info and registering for remote command center actions.
- [class MPNowPlayingSession](mpnowplayingsession.md)
  An object that manages Now Playing information and remote commands for multiple players.
- [class MPNowPlayingInfoCenter](mpnowplayinginfocenter.md)
  An object for setting the Now Playing information for media that your app plays.
- [class MPNowPlayingInfoLanguageOption](mpnowplayinginfolanguageoption.md)
  A set of interfaces for setting the language option for the Now Playing item.
- [Language option characteristic constants](language-option-characteristic-constants.md)
  The constants for defining language characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiongroup)*