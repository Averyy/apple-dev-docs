# stopGroupActivity()

**Framework**: GameKit  
**Kind**: method

Ends a SharePlay activity for the entire group, which the local player activates.

**Availability**:
- iOS 16.2+
- iPadOS 16.2+
- Mac Catalyst 16.2+
- macOS 13.1+
- visionOS 1.0+

## Declaration

```swift
func stopGroupActivity()
```

#### Discussion

Use this method to stop showing a group activity in SharePlay that players use to join a match. This method doesn’t quit the match in your game that players previously join using SharePlay. Players can also stop a group activity using the SharePlay interface.

To start showing a group activity in SharePlay, present a [`GKMatchmakerViewController`](gkmatchmakerviewcontroller.md) object where the player can select SharePlay to invite players, or call the [`startGroupActivity(playerHandler:)`](gkmatchmaker/startgroupactivity(playerhandler:).md) method.

## See Also

- [func startGroupActivity(playerHandler: (GKPlayer) -> Void)](gkmatchmaker/startgroupactivity(playerhandler:).md)
  Begins a SharePlay activity for your game when a FaceTime call is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/stopgroupactivity())*