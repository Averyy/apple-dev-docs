# sendMessage(withLocalizedFormatKey:arguments:data:to:badgePlayers:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Sends a message to players in a game session.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func sendMessage(withLocalizedFormatKey key: String, arguments: [String], data: Data?, to players: [GKCloudPlayer], badgePlayers: Bool) async throws
```

## Parameters

- `key`: A localized string with format tokens.
- `arguments`: An array containing entries for the format tokens contained by the   parameter.
- `data`: A   object containing a limited amount of developer determined game information.
- `players`: A   array containing the players to be messaged.
- `badgePlayers`: A   indicating whether players are badged when the message is sent.
- `completionHandler`: A block that is called after the message has been sent.

## See Also

- [var badgedPlayers: [GKCloudPlayer]](gkgamesession/badgedplayers.md)
  An array containing all of the currently badged players.
- [func clearBadge(for: [GKCloudPlayer], completionHandler: ((any Error)?) -> Void)](gkgamesession/clearbadge(for:completionhandler:).md)
  Clears the badge from the designated players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/sendmessage(withlocalizedformatkey:arguments:data:to:badgeplayers:completionhandler:))*