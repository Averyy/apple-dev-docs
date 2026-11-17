# CPNowPlayingSportsTeamLogo

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A type that manages logo information for a sports team.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
@MainActor
class CPNowPlayingSportsTeamLogo
```

```objc
@interface CPNowPlayingSportsTeamLogo : NSObject
```

## Overview

A `CPNowPlayingSportsTeamLogo` object manages the identifying content for a team. Specify a team’s logo using an image or an abbreviation of the team’s name. For example, an American football team might display an image with the team’s helmet design. CarPlay displays logo information prominently for each team in the Now Playing interface.

Create two `CPNowPlayingSportsTeamLogo` objects during the creation of sports event-related information for the Now Playing interface. Use the logo objects you create to initialize the [`CPNowPlayingSportsTeam`](./cpnowplayingsportsteam.md) objects you use to specify the team information.

## Topics

### Creating a team logo
- [init(teamLogo: UIImage)](./cpnowplayingsportsteamlogo/init%28teamlogo%29.md)
  Creates a logo object using a team-specific image.
- [init(teamInitials: String)](./cpnowplayingsportsteamlogo/init%28teaminitials%29.md)
  Creates a logo object using the team’s initials or the official abbreviation of the team name.
- [init?(coder: NSCoder)](./cpnowplayingsportsteamlogo/init%28coder%29.md)
### Getting the logo content
- [var logo: UIImage?](./cpnowplayingsportsteamlogo/logo.md)
  The image with the team’s logo.
- [var initials: String?](./cpnowplayingsportsteamlogo/initials.md)
  The team’s initials or official team-name abbreviation.

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
- [class CPNowPlayingSportsTeam](./cpnowplayingsportsteam.md)
  A type that specifies team-specific details, including the name, standings, and current score in the match.
- [class CPNowPlayingSportsEventStatus](./cpnowplayingsportseventstatus.md)
  A type that manages match-focused information, including the event clock.
- [class CPNowPlayingSportsClock](./cpnowplayingsportsclock.md)
  A type that specifies the elapsed or remaining time in a match and the state of the clock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsteamlogo)*