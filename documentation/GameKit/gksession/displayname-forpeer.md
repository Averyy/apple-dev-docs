# displayName(forPeer:)

**Framework**: GameKit  
**Kind**: method

Returns a user-readable name for a peer.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func displayName(forPeer peerID: String!) -> String!
```

#### Return Value

The name for the peer, or `nil` if `peerID` is not associated with a visible peer.

#### Discussion

The display name is used to populate your user interface with the names of other peers visible to the session.

## Parameters

- `peerID`: A string that uniquely identifies a peer.

## See Also

- [var displayName: String!](gksession/displayname.md)
  The name of the user.
- [func peers(with: GKPeerConnectionState) -> [Any]!](gksession/peers(with:).md)
  Returns a list of peers in the specified connection state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/displayname(forpeer:))*