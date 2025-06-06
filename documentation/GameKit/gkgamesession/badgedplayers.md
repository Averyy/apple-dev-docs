# badgedPlayers

**Framework**: GameKit  
**Kind**: property

An array containing all of the currently badged players.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var badgedPlayers: [GKCloudPlayer] { get }
```

## See Also

- [func clearBadge(for: [GKCloudPlayer], completionHandler: ((any Error)?) -> Void)](gkgamesession/clearbadge(for:completionhandler:).md)
  Clears the badge from the designated players.
- [func sendMessage(withLocalizedFormatKey: String, arguments: [String], data: Data?, to: [GKCloudPlayer], badgePlayers: Bool, completionHandler: ((any Error)?) -> Void)](gkgamesession/sendmessage(withlocalizedformatkey:arguments:data:to:badgeplayers:completionhandler:).md)
  Sends a message to players in a game session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/badgedplayers)*