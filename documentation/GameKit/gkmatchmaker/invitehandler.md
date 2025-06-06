# inviteHandler

**Framework**: GameKit  
**Kind**: property

A block that GameKit calls when an invitation to join a match is accepted by the local player.

**Availability**:
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
var inviteHandler: ((GKInvite, [Any]?) -> Void)? { get set }
```

#### Discussion

The block takes the following parameters:

Your block needs to respond to the invitation in one of two ways:

- Display the standard user interface by initializing a new [`GKMatchmakerViewController`](gkmatchmakerviewcontroller.md) object, passing the invitation object and the list of player identifiers as parameters.
- Create a match programmatically by calling the [`match(for:completionHandler:)`](gkmatchmaker/match(for:completionhandler:).md) method on the shared matchmaker instance.

If your game receives an invitation while it’s running, it needs to transition to multiplayer play. It must clean up any existing content, such as ending the current match the player is playing, and then process the invitation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/invitehandler)*