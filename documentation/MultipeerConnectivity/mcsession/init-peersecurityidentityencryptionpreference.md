# init(peer:securityIdentity:encryptionPreference:)

**Framework**: Multipeer Connectivity  
**Kind**: init

Creates a Multipeer Connectivity session, providing security information.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(peer myPeerID: MCPeerID, securityIdentity identity: [Any]?, encryptionPreference: MCEncryptionPreference)
```

#### Return Value

The initialized session object, or `nil` if an error occurs.

#### Discussion

All combinations of authentication (supplying an `identity` value or not) and `encryptionPreference` are legal. Using both authentication to establish a peer’s identity and encryption to secure the channel provides the most security, while using neither provides none, but the right combination depends upon the needs of your application. For example, one app might use authentication with unencrypted data if the source of the data must be established, but the data is not sensitive. Another app might use an unauthenticated but encrypted link to avoid eavesdropping among known peers.

This method throws an exception if the provided peer ID object is invalid or `nil`.

For more information, see [`Initiating a Session`](mcsession#Initiating-a-Session.md).

## Parameters

- `myPeerID`: A local identifier that represents the device on which your app is currently running.
- `identity`: When you add other peers to the session, those peers receive your local peer’s certificate (extracted from the provided identity) and any additional certificates that you provided. It is the receiving peer’s responsibility to validate that certificate, if desired.
- `encryptionPreference`: An integer value that indicates whether encryption is required, preferred, or undesirable.

## See Also

- [convenience init(peer: MCPeerID)](mcsession/init(peer:).md)
  Creates a Multipeer Connectivity session.
- [var delegate: (any MCSessionDelegate)?](mcsession/delegate.md)
  The delegate object that handles session-related events.
- [var encryptionPreference: MCEncryptionPreference](mcsession/encryptionpreference.md)
  A value indicating whether the connection prefers encrypted connections, unencrypted connections, or has no preference.
- [var myPeerID: MCPeerID](mcsession/mypeerid.md)
  A local identifier that represents the device on which your app is currently running.
- [var securityIdentity: [Any]?](mcsession/securityidentity.md)
  The security identity of the local peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/init(peer:securityidentity:encryptionpreference:))*