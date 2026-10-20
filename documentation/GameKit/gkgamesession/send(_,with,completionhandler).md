# send(_:with:completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Sends the indicated data to all connected players.

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
func send(_ data: Data, with transport: GKTransportType, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func send(_ data: Data, with transport: GKTransportType) async throws
```

```objc
- (void) sendData:(NSData *) data withTransportType:(GKTransportType) transport completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Parameters

- `data`: A `Data` object containing the information to be sent.
- `transport`: Determines how the data is sent.
- `completionHandler`: A block that is called after the data has been sent.

  - **error**: If an error occurred, this parameter holds an error object that explains the error. Otherwise, the value of this parameter is nil. See `GameKit Constants` for a list of error codes specific to GameKit.

## See Also

### Connecting Players for Real-Time Communication
- [func setConnectionState(GKConnectionState, completionHandler: ((any Error)?) -> Void)](./setconnectionstate%28_,completionhandler%29.md)
  Sets the connection state for the player.
- [func players(with: GKConnectionState) -> [GKCloudPlayer]](./players%28with%29.md)
  Retrieves a list of players with the specified connection state.
- [enum GKTransportType](../gktransporttype.md)
  The mechanism used to send messages to other players in a game session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/send(_:with:completionhandler:))*