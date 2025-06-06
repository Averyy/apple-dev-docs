# matchmakerViewController(_:getMatchPropertiesForRecipient:withCompletionHandler:)

**Framework**: GameKit  
**Kind**: method

Returns the properties for another player that the local player invites using the view controller interface.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.1+

## Declaration

```swift
optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, getMatchPropertiesForRecipient recipient: GKPlayer) async -> [String : Any]
```

## Mentions

- [Finding players using matchmaking rules](finding-players-using-matchmaking-rules.md)

#### Discussion

Implement this method if you can provide properties for the recipients of this match request to better fine tune the Game Center matchmaking using rules. For more information, see [`Matchmaking rules`](matchmaking-rules.md).

## Parameters

- `viewController`: The view controller that finds players for the match.
- `recipient`: A player to invite to the match.
- `completionHandler`: The block receives the following parameter:


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:getmatchpropertiesforrecipient:withcompletionhandler:))*