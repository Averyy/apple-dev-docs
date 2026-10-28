# peers(with:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Returns a list of peers in the specified connection state.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported.

## Declaration

```swift
func peers(with state: GKPeerConnectionState) -> [Any]!
```

```objc
- (NSArray *) peersWithConnectionState:(GKPeerConnectionState) state;
```

## Return Value

An array of [`NSString`](../../Foundation/nsstring.md) objects with a [`peerID`](./peerid.md) string for each peer visible to the session that is currently in the specified connection state. If there are no peers in the specified connection state, this method returns `nil`.

## Parameters

- `state`: The connection state to search for. See [`GKPeerConnectionState`](../gkpeerconnectionstate.md) for possible values.

## See Also

### Obtaining Information About Other Peers
- [func displayName(forPeer: String!) -> String!](./displayname%28forpeer%29.md)
  Returns a user-readable name for a peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/peers(with:))*