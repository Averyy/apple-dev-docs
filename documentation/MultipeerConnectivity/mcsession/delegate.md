# delegate

**Framework**: Multipeer Connectivity  
**Kind**: property

The delegate object that handles session-related events.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any MCSessionDelegate)? { get set }
```

## See Also

- [convenience init(peer: MCPeerID)](mcsession/init(peer:).md)
  Creates a Multipeer Connectivity session.
- [init(peer: MCPeerID, securityIdentity: [Any]?, encryptionPreference: MCEncryptionPreference)](mcsession/init(peer:securityidentity:encryptionpreference:).md)
  Creates a Multipeer Connectivity session, providing security information.
- [var encryptionPreference: MCEncryptionPreference](mcsession/encryptionpreference.md)
  A value indicating whether the connection prefers encrypted connections, unencrypted connections, or has no preference.
- [var myPeerID: MCPeerID](mcsession/mypeerid.md)
  A local identifier that represents the device on which your app is currently running.
- [var securityIdentity: [Any]?](mcsession/securityidentity.md)
  The security identity of the local peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/delegate)*