# CPNowPlayingSportsTeam

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A type that specifies team-specific details, including the name, standings, and current score in the match.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
@MainActor
class CPNowPlayingSportsTeam
```

```objc
@interface CPNowPlayingSportsTeam : NSObject
```

## Overview

A `CPNowPlayingSportsTeam` object manages the details for one of the opponents in a match. This type stores team-specific information, such as the team’s name, logo artwork, their standings, and whether it’s a person’s favorite team. This type also stores the current score for the team, which you update each time the team scores. CarPlay displays team information prominently in the Now Playing interface on the left or ride side of the display.

At the start of a match, create two `CPNowPlayingSportsTeam` objects and fill them with information about the opposing teams. To display the team information in the Now Playing interface, create a [`CPNowPlayingModeSports`](./cpnowplayingmodesports.md) object, initialize it with the teams you created, and assign it to the [`nowPlayingMode`](./cpnowplayingtemplate/nowplayingmode.md) property of the shared [`CPNowPlayingTemplate`](./cpnowplayingtemplate.md) object. When the score changes during the match, recreate the team objects with the new score values and update the object in the [`nowPlayingMode`](./cpnowplayingtemplate/nowplayingmode.md) property.

## Topics

### Creating a sports team object
- [init(name: String, logo: CPNowPlayingSportsTeamLogo, teamStandings: String?, eventScore: String, possessionIndicator: UIImage?, favorite: Bool)](./cpnowplayingsportsteam/init%28name,logo,teamstandings,eventscore,possessionindicator,favorite%29.md)
  Creates an object using a team’s name, logo, and other information.
- [init?(coder: NSCoder)](./cpnowplayingsportsteam/init%28coder%29.md)
### Getting the team information
- [var name: String](./cpnowplayingsportsteam/name.md)
  The localized name of the team.
- [var logo: CPNowPlayingSportsTeamLogo](./cpnowplayingsportsteam/logo.md)
  The logo information for the team.
- [var isFavorite: Bool](./cpnowplayingsportsteam/isfavorite.md)
  A Boolean value that indicates whether the team is one of the person’s favorites.
- [var teamStandings: String?](./cpnowplayingsportsteam/teamstandings.md)
  Team-specific information to display with the team’s name and logo.
### Getting match-related details
- [var eventScore: String](./cpnowplayingsportsteam/eventscore.md)
  The number of points or current score for the team.
- [var possessionIndicator: UIImage?](./cpnowplayingsportsteam/possessionindicator.md)
  An optional image to display next to the team in possession of the ball.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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

## See Also

### Sports mode content
- [class CPNowPlayingSportsTeamLogo](./cpnowplayingsportsteamlogo.md)
  A type that manages logo information for a sports team.
- [class CPNowPlayingSportsEventStatus](./cpnowplayingsportseventstatus.md)
  A type that manages match-focused information, including the event clock.
- [class CPNowPlayingSportsClock](./cpnowplayingsportsclock.md)
  A type that specifies the elapsed or remaining time in a match and the state of the clock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsteam)*