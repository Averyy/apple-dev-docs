# clearBadge(for:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Clears the badge from the designated players.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func clearBadge(for players: [GKCloudPlayer]) async throws
```

## Parameters

- `players`: An array of GKCloudPlayers identifying the players that are to have their badge removed.
- `completionHandler`: A block that is called after the badges have been removed from the players.

## See Also

- [var badgedPlayers: [GKCloudPlayer]](gkgamesession/badgedplayers.md)
  An array containing all of the currently badged players.
- [func sendMessage(withLocalizedFormatKey: String, arguments: [String], data: Data?, to: [GKCloudPlayer], badgePlayers: Bool, completionHandler: ((any Error)?) -> Void)](gkgamesession/sendmessage(withlocalizedformatkey:arguments:data:to:badgeplayers:completionhandler:).md)
  Sends a message to players in a game session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/clearbadge(for:completionhandler:))*