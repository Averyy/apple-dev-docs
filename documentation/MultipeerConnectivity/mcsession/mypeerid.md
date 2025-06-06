# myPeerID

**Framework**: Multipeer Connectivity  
**Kind**: property

A local identifier that represents the device on which your app is currently running.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var myPeerID: MCPeerID { get }
```

#### Discussion

You set this value when you initialize the session object. It cannot be changed later.

## See Also

- [convenience init(peer: MCPeerID)](mcsession/init(peer:).md)
  Creates a Multipeer Connectivity session.
- [init(peer: MCPeerID, securityIdentity: [Any]?, encryptionPreference: MCEncryptionPreference)](mcsession/init(peer:securityidentity:encryptionpreference:).md)
  Creates a Multipeer Connectivity session, providing security information.
- [var delegate: (any MCSessionDelegate)?](mcsession/delegate.md)
  The delegate object that handles session-related events.
- [var encryptionPreference: MCEncryptionPreference](mcsession/encryptionpreference.md)
  A value indicating whether the connection prefers encrypted connections, unencrypted connections, or has no preference.
- [var securityIdentity: [Any]?](mcsession/securityidentity.md)
  The security identity of the local peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/mypeerid)*