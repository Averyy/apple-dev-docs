# loadPlayers(forIdentifiers:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method

Loads information about a list of players from Game Center.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func loadPlayers(forIdentifiers identifiers: [String], withCompletionHandler completionHandler: (([GKPlayer]?, (any Error)?) -> Void)? = nil)
```

## Parameters

- `identifiers`: The identifiers for the players to load.
- `completionHandler`: The block that GameKit calls when it completes the request. The block receives the following parameters: - ***players***: The players that GameKit successfully loads. If an error occurs, this array may contain just the player data that GameKit is able to load.
- ***error***: Describes an error if it occurs, or `nil` if the operation completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkplayer/loadplayers(foridentifiers:withcompletionhandler:))*