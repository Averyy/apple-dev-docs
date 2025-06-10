# GKGameActivityListener

**Framework**: GameKit  
**Kind**: protocol

An object that responds to activity events.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol GKGameActivityListener
```

## Mentions

- [Creating activities for your game](creating-activities-for-your-game.md)

## Topics

### Responding to an activity
- [func player(GKPlayer, wantsToPlay: GKGameActivity, completionHandler: (Bool) -> Void)](gkgameactivitylistener/player(_:wantstoplay:completionhandler:).md)
  Called when a player intends to play for a specific game activity. A completion handler block is provided to indicate whether the activity was successfully handled.

## Relationships

### Inherited By
- [GKLocalPlayerListener](gklocalplayerlistener.md)

## See Also

- [Creating activities for your game](creating-activities-for-your-game.md)
  Use activities to surface game content to players and encourage them to connect with each other.
- [class GKGameActivity](gkgameactivity.md)
  An object that represents a single instance of a game activity for the current game.
- [class GKGameActivityDefinition](gkgameactivitydefinition.md)
  An object that represents the static metadata you define for the activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivitylistener)*