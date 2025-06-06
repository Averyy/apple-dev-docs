# startBrowsingForNearbyPlayers(handler:)

**Framework**: GameKit  
**Kind**: method

Finds nearby players through Bluetooth or WiFi on the same subnet.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func startBrowsingForNearbyPlayers(handler reachableHandler: ((GKPlayer, Bool) -> Void)? = nil)
```

#### Discussion

Use the `reachableHandler` implementation to update your interface with information about nearby players. If the local player wants to invite a nearby player, call the [`findMatch(for:withCompletionHandler:)`](gkmatchmaker/findmatch(for:withcompletionhandler:).md) method to create a match or the [`addPlayers(to:matchRequest:completionHandler:)`](gkmatchmaker/addplayers(to:matchrequest:completionhandler:).md) method to update an existing match. When you are done finding nearby players, call the [`stopBrowsingForNearbyPlayers()`](gkmatchmaker/stopbrowsingfornearbyplayers().md) method.

> **Note**:  Before your game is released and during development, GameKit invokes the handler for all nearby players of all Game Center games.

 Before your game is released and during development, GameKit invokes the handler for all nearby players of all Game Center games.

## Parameters

- `reachableHandler`: This block receives the following parameters:

## See Also

- [func stopBrowsingForNearbyPlayers()](gkmatchmaker/stopbrowsingfornearbyplayers.md)
  Stops finding nearby players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/startbrowsingfornearbyplayers(handler:))*