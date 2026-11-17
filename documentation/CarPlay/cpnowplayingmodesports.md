# CPNowPlayingModeSports

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A mode that manages the sporting event details to display in the Now Playing interface.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
@MainActor
class CPNowPlayingModeSports
```

```objc
@interface CPNowPlayingModeSports : CPNowPlayingMode
```

## Overview

The `CPNowPlayingModeSports` type reconfigures the Now Playing interface to display information from a sporting event. This type is for apps that want to show information about the sporting event while they play event-related audio. When you apply this mode to your app’s [`CPNowPlayingTemplate`](./cpnowplayingtemplate.md) object, the Now Playing interface displays match information you specify instead of information about the current audio track. For example, while your app plays audio for a football match, the interface displays the team names and logos, the current score, and the elapsed or remaining time.

At the start of a sporting event, create an instance of this type and configure it with the team information and other event details. To display the information, assign your `CPNowPlayingModeSports` object to the [`nowPlayingMode`](./cpnowplayingtemplate/nowplayingmode.md) property of your app’s [`CPNowPlayingTemplate`](./cpnowplayingtemplate.md) object. As the event progresses, update the team and event information to reflect changes to the score or match state. For example, update the game clock information when gameplay pauses or resumes. When the match ends, restore the [`default`](./cpnowplayingmode/default.md) mode to the [`CPNowPlayingTemplate`](./cpnowplayingtemplate.md) object to return the interface to its standard configuration.

Play audio or video for a match using the [Media Player](../MediaPlayer/MediaPlayer.md) or [AVKit](../AVKit/AVKit.md) framework. Each framework has its own form of Now Playing support, which CarPlay uses to manage interactions with the controls of the Now Playing interface.

## Topics

### Creating a sports mode type
- [init(leftTeam: CPNowPlayingSportsTeam, rightTeam: CPNowPlayingSportsTeam, eventStatus: CPNowPlayingSportsEventStatus?, backgroundArtwork: UIImage?)](./cpnowplayingmodesports/init%28leftteam,rightteam,eventstatus,backgroundartwork%29.md)
  Creates an object with information about a sporting event and the teams playing.
### Getting the event details
- [var leftTeam: CPNowPlayingSportsTeam](./cpnowplayingmodesports/leftteam.md)
  Team-specific details to display on the left side of the Now Playing interface.
- [var rightTeam: CPNowPlayingSportsTeam](./cpnowplayingmodesports/rightteam.md)
  Details for the team that appears on the right side of the display.
- [var eventStatus: CPNowPlayingSportsEventStatus?](./cpnowplayingmodesports/eventstatus.md)
  Match details to display in the center of the Now Playing interface.
- [var backgroundArtwork: UIImage?](./cpnowplayingmodesports/backgroundartwork.md)
  The image to display behind the match information.

## Relationships

### Inherits From
- [CPNowPlayingMode](./cpnowplayingmode.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Interface modes
- [class CPNowPlayingMode](./cpnowplayingmode.md)
  A type that defines the appearance and layout of the Now Playing interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingmodesports)*