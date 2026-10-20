# sendMessage(withLocalizedFormatKey:arguments:data:to:badgePlayers:completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Sends a message to players in a game session.

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
func sendMessage(withLocalizedFormatKey key: String, arguments: [String], data: Data?, to players: [GKCloudPlayer], badgePlayers: Bool, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func sendMessage(withLocalizedFormatKey key: String, arguments: [String], data: Data?, to players: [GKCloudPlayer], badgePlayers: Bool) async throws
```

```objc
- (void) sendMessageWithLocalizedFormatKey:(NSString *) key arguments:(NSArray<NSString *> *) arguments data:(NSData *) data toPlayers:(NSArray<GKCloudPlayer *> *) players badgePlayers:(BOOL) badgePlayers completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Parameters

- `key`: A localized string with format tokens.
- `arguments`: An array containing entries for the format tokens contained by the `key` parameter.
- `data`: A `Data` object containing a limited amount of developer determined game information.
- `players`: A `GKCloudPlayer` array containing the players to be messaged.
- `badgePlayers`: A `Boolean` indicating whether players are badged when the message is sent.
- `completionHandler`: A block that is called after the message has been sent.

  - **error**: If an error occurred, this parameter holds an error object that explains the error. Otherwise, the value of this parameter is nil. See `GameKit Constants` for a list of error codes specific to GameKit.

## See Also

### Communicating Between Players
- [var badgedPlayers: [GKCloudPlayer]](./badgedplayers.md)
  An array containing all of the currently badged players.
- [func clearBadge(for: [GKCloudPlayer], completionHandler: ((any Error)?) -> Void)](./clearbadge%28for,completionhandler%29.md)
  Clears the badge from the designated players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/sendmessage(withlocalizedformatkey:arguments:data:to:badgeplayers:completionhandler:))*