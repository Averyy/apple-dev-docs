# loadPlayers(forIdentifiers:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Loads information about a list of players from Game Center.

**Availability**:
- iOS 4.1+ - Deprecated in 14.5
- iPadOS 4.1+ - Deprecated in 14.5
- Mac Catalyst 13.1+ - Deprecated in 14.5
- macOS 10.8+ - Deprecated in 11.3
- tvOS 9.0+ - Deprecated in 14.5
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 7.4

> **Deprecated**: Use [`loadFriends(identifiedBy:completionHandler:)`](../gklocalplayer/loadfriends%28identifiedby,completionhandler%29.md) instead.

## Declaration

```swift
class func loadPlayers(forIdentifiers identifiers: [String], withCompletionHandler completionHandler: (([GKPlayer]?, (any Error)?) -> Void)? = nil)
```

```objc
+ (void) loadPlayersForIdentifiers:(NSArray<NSString *> *) identifiers withCompletionHandler:(void (^)(NSArray<GKPlayer *> *players, NSError *error)) completionHandler;
```

## Parameters

- `identifiers`: The identifiers for the players to load.
- `completionHandler`: The block that GameKit calls when it completes the request.

  The block receives the following parameters:

  - ***players***: The players that GameKit successfully loads. If an error occurs, this array may contain just the player data that GameKit is able to load.
  - ***error***: Describes an error if it occurs, or `nil` if the operation completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkplayer/loadplayers(foridentifiers:withcompletionhandler:))*