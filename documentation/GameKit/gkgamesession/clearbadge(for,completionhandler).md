# clearBadge(for:completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Clears the badge from the designated players.

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
func clearBadge(for players: [GKCloudPlayer], completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func clearBadge(for players: [GKCloudPlayer]) async throws
```

```objc
- (void) clearBadgeForPlayers:(NSArray<GKCloudPlayer *> *) players completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Parameters

- `players`: An array of GKCloudPlayers identifying the players that are to have their badge removed.
- `completionHandler`: A block that is called after the badges have been removed from the players.

  - **error**: If an error occurred, this parameter holds an error object that explains the error. Otherwise, the value of this parameter is nil. See `GameKit Constants` for a list of error codes specific to GameKit.

## See Also

### Communicating Between Players
- [var badgedPlayers: [GKCloudPlayer]](./badgedplayers.md)
  An array containing all of the currently badged players.
- [func sendMessage(withLocalizedFormatKey: String, arguments: [String], data: Data?, to: [GKCloudPlayer], badgePlayers: Bool, completionHandler: ((any Error)?) -> Void)](./sendmessage%28withlocalizedformatkey,arguments,data,to,badgeplayers,completionhandler%29.md)
  Sends a message to players in a game session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/clearbadge(for:completionhandler:))*