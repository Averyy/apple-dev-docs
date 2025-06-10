# GKGameActivity

**Framework**: GameKit  
**Kind**: class

An object that represents a single instance of a game activity for the current game.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class GKGameActivity
```

## Mentions

- [Creating activities for your game](creating-activities-for-your-game.md)

## Topics

### Creating an activity
- [init(definition: GKGameActivityDefinition)](gkgameactivity/init(definition:).md)
  Initializes a game activity with definition.
- [class func start(definition: GKGameActivityDefinition) throws -> GKGameActivity](gkgameactivity/start(definition:).md)
  Initializes and starts a game activity with definition.
- [class func start(definition: GKGameActivityDefinition, partyCode: String) throws -> GKGameActivity](gkgameactivity/start(definition:partycode:).md)
  Creates and starts a new game activity with a custom party code.
### Getting the activity definition
- [var activityDefinition: GKGameActivityDefinition](gkgameactivity/activitydefinition.md)
  The activity definition that this activity instance is based on.
### Getting the activity state
- [var state: GKGameActivity.State](gkgameactivity/state-swift.property.md)
  The state of the game activity.
- [GKGameActivity.State](gkgameactivity/state-swift.enum.md)
### Updating the activity state
- [func start()](gkgameactivity/start.md)
  Starts the game activity if it is not already started.
- [func pause()](gkgameactivity/pause.md)
  Pauses the game activity if it is not already paused.
- [func resume()](gkgameactivity/resume.md)
  Resumes the game activity if it was paused.
- [func end()](gkgameactivity/end.md)
  Ends the game activity if it is not already ended.
### Getting and removing achievements
- [var achievements: Set<GKAchievement>](gkgameactivity/achievements.md)
  All achievements that have been associated with this activity.
- [func removeAchievements([GKAchievement])](gkgameactivity/removeachievements(_:).md)
  Removes all achievements if exist.
- [func progress(on: GKAchievement) -> Double](gkgameactivity/progress(on:).md)
  Get the achievement progress from a specific achievement of the local player if previously set.
- [func setProgress(on: GKAchievement, to: Double)](gkgameactivity/setprogress(on:to:).md)
  Set a progress for an achievement for a player.
- [func setAchievementCompleted(GKAchievement)](gkgameactivity/setachievementcompleted(_:).md)
  Convenience method to set a progress to 100% for an achievement for a player.
### Getting and removing leaderboard scores
- [var leaderboardScores: Set<GKLeaderboardScore>](gkgameactivity/leaderboardscores.md)
  All leaderboard scores that have been associated with this activity.
- [func score(on: GKLeaderboard) -> GKLeaderboardScore?](gkgameactivity/score(on:).md)
  Get the leaderboard score from a specific leaderboard of the local player if previously set.
- [func setScore(on: GKLeaderboard, to: Int)](gkgameactivity/setscore(on:to:).md)
  Set a score of a leaderboard for a player.
- [func setScore(on: GKLeaderboard, to: Int, context: Int)](gkgameactivity/setscore(on:to:context:).md)
  Set a score of a leaderboard with a context for a player.
- [func removeScores(from: [GKLeaderboard])](gkgameactivity/removescores(from:).md)
  Removes all scores from leaderboards for a player if exist.
### Getting and verifying the party code
- [var partyCode: String?](gkgameactivity/partycode.md)
  If the game supports party code, this is the party code that can be shared among players to join the party.
- [var partyURL: URL?](gkgameactivity/partyurl.md)
  If the game supports party code, this is the URL that can be shared among players to join the party.
- [class var validPartyCodeAlphabet: [String]](gkgameactivity/validpartycodealphabet.md)
  Allowed characters for the party code to be used to share this activity.
- [class func isValidPartyCode(String) -> Bool](gkgameactivity/isvalidpartycode(_:).md)
  Checks whether a party code is in valid format.
### Getting the activity properties
- [var duration: TimeInterval](gkgameactivity/duration.md)
  Total time elapsed while in active state.
- [var startDate: Date?](gkgameactivity/startdate.md)
  The date when the activity was initially started.
- [var endDate: Date?](gkgameactivity/enddate.md)
  The date when the activity was officially ended.
- [var creationDate: Date](gkgameactivity/creationdate.md)
  The date when the activity was created.
- [var lastResumeDate: Date?](gkgameactivity/lastresumedate.md)
  The date when the activity was last resumed.
### Getting the custom user data
- [var properties: [String : String]](gkgameactivity/properties.md)
  Properties that contain additional information about the activity.
### Getting the activity identifiers
- [var identifier: String](gkgameactivity/identifier.md)
  The identifier of this activity instance.
### Checking for an activity
- [class func checkPendingGameActivityExistence(completionHandler: (Bool) -> Void)](gkgameactivity/checkpendinggameactivityexistence(completionhandler:).md)
  Checks whether there is a pending activity to handle for the current game.
### Creating a matchmaking request
- [func makeMatchRequest() -> GKMatchRequest?](gkgameactivity/makematchrequest.md)
  Makes a `GKMatchRequest` object with information from the activity, which can be used to find matches for the local player.
### Performing a matchmaking request
- [func findMatch(completionHandler: (GKMatch?, (any Error)?) -> Void)](gkgameactivity/findmatch(completionhandler:).md)
  Use information from the activity to find matches for the local player.
- [func findPlayersForHostedMatch(completionHandler: ([GKPlayer]?, (any Error)?) -> Void)](gkgameactivity/findplayersforhostedmatch(completionhandler:).md)
  Use information from the activity to find server hosted players for the local player.

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
- [class GKGameActivityDefinition](gkgameactivitydefinition.md)
  An object that represents the static metadata you define for the activity.
- [protocol GKGameActivityListener](gkgameactivitylistener.md)
  An object that responds to activity events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity)*