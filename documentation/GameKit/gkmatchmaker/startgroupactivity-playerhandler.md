# startGroupActivity(playerHandler:)

**Framework**: GameKit  
**Kind**: method

Begins a SharePlay activity for your game when a FaceTime call is active.

**Availability**:
- iOS 16.2+
- iPadOS 16.2+
- Mac Catalyst 16.2+
- macOS 13.1+
- visionOS 1.0+

## Declaration

```swift
func startGroupActivity(playerHandler handler: @escaping (GKPlayer) -> Void)
```

## Mentions

- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)
- [Adding voice chat to multiplayer games](adding-voice-chat-to-multiplayer-games.md)

#### Discussion

SharePlay lets people share experiences in a group activity, such as joining your game using FaceTime or the Messages app. If you implement a custom group activity interface, use this method to show a group activity that your game provides in apps that support the SharePlay interface. For macOS apps, add the Group Activities capability to your Xcode to enable this feature.

To start a group activity on behalf of the player and receive callbacks for each player that joins, invoke the [`startGroupActivity(playerHandler:)`](gkmatchmaker/startgroupactivity(playerhandler:).md) method. Implement the handler to add each player that joins to the match before starting gameplay using the [`addPlayers(to:matchRequest:completionHandler:)`](gkmatchmaker/addplayers(to:matchrequest:completionhandler:).md) method.

If an app with a SharePlay interface isn’t running when you invoke the [`startGroupActivity(playerHandler:)`](gkmatchmaker/startgroupactivity(playerhandler:).md) method, GameKit presents an interface that lets the player share a group activity in an app that supports SharePlay. Then the player can stop showing the group activity using the SharePlay interface, or you can stop the group activity on behalf of the player using the [`stopGroupActivity()`](gkmatchmaker/stopgroupactivity().md) method.

Alternatively, if you want to present a familiar GameKit interface, instead present a [`GKMatchmakerViewController`](gkmatchmakerviewcontroller.md) object that lets the player start a group activity by selecting SharePlay to invite players.

## Parameters

- `handler`: This block receives the following parameter:

## See Also

- [func stopGroupActivity()](gkmatchmaker/stopgroupactivity.md)
  Ends a SharePlay activity for the entire group, which the local player activates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/startgroupactivity(playerhandler:))*