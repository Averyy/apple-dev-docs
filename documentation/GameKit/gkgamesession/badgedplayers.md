# badgedPlayers

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

An array containing all of the currently badged players.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0
- iPadOS 10.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.14
- tvOS 10.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: For real-time matches, use GKMatchmakerViewController. For turn-based matches, use GKTurnBasedMatchmakerViewController.

## Declaration

```swift
var badgedPlayers: [GKCloudPlayer] { get }
```

```objc
@property (nonatomic, readonly) NSArray<GKCloudPlayer *> * badgedPlayers;
```

## See Also

### Communicating Between Players
- [func clearBadge(for: [GKCloudPlayer], completionHandler: ((any Error)?) -> Void)](./clearbadge%28for,completionhandler%29.md)
  Clears the badge from the designated players.
- [func sendMessage(withLocalizedFormatKey: String, arguments: [String], data: Data?, to: [GKCloudPlayer], badgePlayers: Bool, completionHandler: ((any Error)?) -> Void)](./sendmessage%28withlocalizedformatkey,arguments,data,to,badgeplayers,completionhandler%29.md)
  Sends a message to players in a game session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/badgedplayers)*