# nearbyConnectionData(forPeer:withCompletionHandler:)

**Framework**: Multipeer Connectivity  
**Kind**: method

Obtains connection data for the specified peer.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func nearbyConnectionData(forPeer peerID: MCPeerID) async throws -> Data
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func nearbyConnectionData(forPeer peerID: MCPeerID) async throws -> Data
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func nearbyConnectionData(forPeer peerID: MCPeerID) async throws -> Data
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

This method provides connection data that is required when adding a specific nearby peer to a session if you are using your own service discovery code instead of an `MCNearbyServiceBrowser` or `MCBrowserViewController` object. For more information, see the [`Managing Peers Manually`](mcsession#Managing-Peers-Manually.md) section in the overview of the `MCSession` class reference.

## Parameters

- `peerID`: A peer ID object obtained from the nearby peer that you want to add to a session.
- `completionHandler`: A handler that is called when connection data is available or when an error occurs.

## See Also

- [func connectPeer(MCPeerID, withNearbyConnectionData: Data)](mcsession/connectpeer(_:withnearbyconnectiondata:).md)
  Call this method to connect a peer to the session when using your own service discovery code instead of an  `MCNearbyServiceBrowser` or `MCBrowserViewController` object.
- [func cancelConnectPeer(MCPeerID)](mcsession/cancelconnectpeer(_:).md)
  Cancels an attempt to connect to a peer.
- [var connectedPeers: [MCPeerID]](mcsession/connectedpeers.md)
  An array of all peers that are currently connected to this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/nearbyconnectiondata(forpeer:withcompletionhandler:))*