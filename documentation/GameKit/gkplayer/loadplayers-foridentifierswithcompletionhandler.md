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
- `completionHandler`: The block receives the following parameters:


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkplayer/loadplayers(foridentifiers:withcompletionhandler:))*