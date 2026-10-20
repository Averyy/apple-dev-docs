# CPNowPlayingSportsTeam

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A representation of a sports team for the now playing screen, in sports that have exactly two teams.

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

## Topics

### Initializers
- [init?(coder: NSCoder)](./cpnowplayingsportsteam/init%28coder%29.md)
- [init(name: String, logo: CPNowPlayingSportsTeamLogo, teamStandings: String?, eventScore: String, possessionIndicator: UIImage?, favorite: Bool)](./cpnowplayingsportsteam/init%28name,logo,teamstandings,eventscore,possessionindicator,favorite%29.md)
  Initialize a sports team for display on the now playing screen.
### Instance Properties
- [var eventScore: String](./cpnowplayingsportsteam/eventscore.md)
  The numeric score string for this team in the current event. Depending on the size of the car screen, a maximum of 3 to 5 characters may be displayed.
- [var isFavorite: Bool](./cpnowplayingsportsteam/isfavorite.md)
  If true, the team is marked with a star to indicate it has been saved as a user favorite.
- [var logo: CPNowPlayingSportsTeamLogo](./cpnowplayingsportsteam/logo.md)
  The team logo or, if no logo is available, the initials/abbreviation for this team. See @c CPNowPlayingSportsTeamLogo.
- [var name: String](./cpnowplayingsportsteam/name.md)
  A localized, user-visible name for this sports team.
- [var possessionIndicator: UIImage?](./cpnowplayingsportsteam/possessionindicator.md)
  An optional indicator used to indicate possession by this team. Only one team should have possession at a given time.
- [var teamStandings: String?](./cpnowplayingsportsteam/teamstandings.md)
  An optional additional label displayed near the team name. This could be a win-loss ratio string, team standings, or other statistics relevant to this team. Depending on the size of the car screen, a maximum of 15-20 characters may be displayed.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsteam)*