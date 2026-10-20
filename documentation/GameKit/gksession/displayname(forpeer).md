# displayName(forPeer:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Returns a user-readable name for a peer.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```swift
func displayName(forPeer peerID: String!) -> String!
```

```objc
- (NSString *) displayNameForPeer:(NSString *) peerID;
```

#### Return Value

The name for the peer, or `nil` if `peerID` is not associated with a visible peer.

#### Discussion

The display name is used to populate your user interface with the names of other peers visible to the session.

## Parameters

- `peerID`: A string that uniquely identifies a peer.

## See Also

### Related Documentation
- [var displayName: String!](./displayname.md)
  The name of the user.
### Obtaining Information About Other Peers
- [func peers(with: GKPeerConnectionState) -> [Any]!](./peers%28with%29.md)
  Returns a list of peers in the specified connection state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/displayname(forpeer:))*