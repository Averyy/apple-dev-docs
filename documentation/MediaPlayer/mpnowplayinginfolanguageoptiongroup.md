# MPNowPlayingInfoLanguageOptionGroup

**Framework**: Media Player  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPNowPlayingInfoLanguageOptionGroup : NSObject
```

## Overview

The `MPNowPlayingInfoLanguageOptionGroup` and [`MPNowPlayingInfoLanguageOption`](./mpnowplayinginfolanguageoption.md) classes provide interfaces for setting information about language options, for example, audio and subtitles, in the Now Playing information area.

## Topics

### Creating a new language option group
- [init(languageOptions: [MPNowPlayingInfoLanguageOption], defaultLanguageOption: MPNowPlayingInfoLanguageOption?, allowEmptySelection: Bool)](./mpnowplayinginfolanguageoptiongroup/init%28languageoptions,defaultlanguageoption,allowemptyselection%29.md)
  Creates a new language option group with the supplied language options.
### Retrieving language option group information
- [var allowEmptySelection: Bool](./mpnowplayinginfolanguageoptiongroup/allowemptyselection.md)
  A Boolean that indicates whether the system requires a selection for the language option group.
- [var defaultLanguageOption: MPNowPlayingInfoLanguageOption?](./mpnowplayinginfolanguageoptiongroup/defaultlanguageoption.md)
  The default language option for the group.
- [var languageOptions: [MPNowPlayingInfoLanguageOption]](./mpnowplayinginfolanguageoptiongroup/languageoptions.md)
  The available language options for the group.

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
- [class MPNowPlayingInfoLanguageOption](./mpnowplayinginfolanguageoption.md)
  A set of interfaces for setting the language option for the Now Playing item.
- [Language option characteristic constants](./language-option-characteristic-constants.md)
  The constants for defining language characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiongroup)*