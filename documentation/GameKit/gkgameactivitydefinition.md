# GKGameActivityDefinition

**Framework**: GameKit  
**Kind**: class

An object that represents the static metadata you define for the activity.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class GKGameActivityDefinition
```

## Mentions

- [Creating activities for your game](creating-activities-for-your-game.md)

## Topics

### Getting the display properties and image
- [var title: String](gkgameactivitydefinition/title.md)
  A short title for the game activity.
- [var details: String?](gkgameactivitydefinition/details.md)
  A more detailed description of the game activity.
- [var defaultProperties: [String : String]](gkgameactivitydefinition/defaultproperties.md)
  Default properties defined by the developer for this type of game activity.
- [func loadImage(completionHandler: (UIImage?, (any Error)?) -> Void)](gkgameactivitydefinition/loadimage(completionhandler:).md)
  Asynchronously load the image. Error will be nil on success.
### Getting the activity capabilities
- [var supportsPartyCode: Bool](gkgameactivitydefinition/supportspartycode.md)
  Whether the activity can be joined by others via a party code.
- [var supportsUnlimitedPlayers: Bool](gkgameactivitydefinition/supportsunlimitedplayers.md)
  True if the activity supports an unlimited number of players. False if maxPlayers is set to a defined limit or if no player range is provided.
- [var playerRange: (any RangeExpression)?](gkgameactivitydefinition/playerrange.md)
  The range of players supported by this type of game activity.
- [var playStyle: GKGameActivityPlayStyle](gkgameactivitydefinition/playstyle.md)
  The play style of the game activity.
- [enum GKGameActivityPlayStyle](gkgameactivityplaystyle.md)
  Play Style of the game activity. It can be either Asynchronous or Synchronous.
### Getting the fallback URL
- [var fallbackURL: URL?](gkgameactivitydefinition/fallbackurl.md)
  A fallback URL that can be used to construct a game-specific URL for players to share or join, if the joining device does not support the default URL.
### Getting the release state
- [var releaseState: GKReleaseState](gkgameactivitydefinition/releasestate.md)
  The release state of the game activity definition in App Store Connect.
- [struct GKReleaseState](gkreleasestate.md)
  Describes the release state of an App Store Connect resource, such as an Achievement or Leaderboard.
### Getting the identifier properties
- [var identifier: String](gkgameactivitydefinition/identifier.md)
  The developer defined identifier for a given game activity.
- [var groupIdentifier: String?](gkgameactivitydefinition/groupidentifier.md)
  The group identifier for the activity, if one exists.
### Loading activity definitions
- [class func loadGameActivityDefinitions(completionHandler: ([GKGameActivityDefinition]?, (any Error)?) -> Void)](gkgameactivitydefinition/loadgameactivitydefinitions(completionhandler:).md)
  Loads all the game activity definitions for the current game.
### Loading achievement descriptions
- [func loadAchievementDescriptions(completionHandler: ([GKAchievementDescription]?, (any Error)?) -> Void)](gkgameactivitydefinition/loadachievementdescriptions(completionhandler:).md)
  Loads all associated achievements that have defined deep links to this game activity definition.
### Loading leaderboards
- [func loadLeaderboards(completionHandler: ([GKLeaderboard]?, (any Error)?) -> Void)](gkgameactivitydefinition/loadleaderboards(completionhandler:).md)
  Loads all associated leaderboards that have defined deep links to this game activity definition.
### Type Methods
- [class func loadGameActivityDefinitions(IDs: [String]?, completionHandler: ([GKGameActivityDefinition]?, (any Error)?) -> Void)](gkgameactivitydefinition/loadgameactivitydefinitions(ids:completionhandler:).md)
  Loads game activity definitions with the supplied App Store Connect identifiers.

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Creating activities for your game](creating-activities-for-your-game.md)
  Use activities to surface game content to players and encourage them to connect with each other.
- [class GKGameActivity](gkgameactivity.md)
  An object that represents a single instance of a game activity for the current game.
- [protocol GKGameActivityListener](gkgameactivitylistener.md)
  An object that responds to activity events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivitydefinition)*