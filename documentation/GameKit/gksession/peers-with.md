# peers(with:)

**Framework**: GameKit  
**Kind**: method

Returns a list of peers in the specified connection state.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func peers(with state: GKPeerConnectionState) -> [Any]!
```

#### Return Value

An array of [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects with a [`peerID`](gksession/peerid.md) string for each peer visible to the session that is currently in the specified connection state. If there are no peers in the specified connection state, this method returns `nil`.

## Parameters

- `state`: The connection state to search for. See   for possible values.

## See Also

- [func displayName(forPeer: String!) -> String!](gksession/displayname(forpeer:).md)
  Returns a user-readable name for a peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/peers(with:))*