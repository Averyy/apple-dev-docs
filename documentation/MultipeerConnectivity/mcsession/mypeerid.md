# myPeerID

**Framework**: Multipeer Connectivity  
**Kind**: property  
**Role**: Instance Property

A local identifier that represents the device on which your app is currently running.

**Availability**:
- iOS 7.0+ - Deprecated in 27.0
- iPadOS 7.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use Network Framework instead

## Declaration

```swift
var myPeerID: MCPeerID { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, readonly) MCPeerID * myPeerID;
```

*macOS*

```objc
@property (atomic, readonly) MCPeerID * myPeerID;
```

#### Discussion

You set this value when you initialize the session object. It cannot be changed later.

## See Also

### Creating a Session
- [convenience init(peer: MCPeerID)](./init%28peer%29.md)
  Creates a Multipeer Connectivity session.
- [init(peer: MCPeerID, securityIdentity: [Any]?, encryptionPreference: MCEncryptionPreference)](./init%28peer,securityidentity,encryptionpreference%29.md)
  Creates a Multipeer Connectivity session, providing security information.
- [var delegate: (any MCSessionDelegate)?](./delegate.md)
  The delegate object that handles session-related events.
- [var encryptionPreference: MCEncryptionPreference](./encryptionpreference.md)
  A value indicating whether the connection prefers encrypted connections, unencrypted connections, or has no preference.
- [var securityIdentity: [Any]?](./securityidentity.md)
  The security identity of the local peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/mypeerid)*