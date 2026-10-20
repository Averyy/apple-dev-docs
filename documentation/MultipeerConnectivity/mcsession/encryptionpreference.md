# encryptionPreference

**Framework**: Multipeer Connectivity  
**Kind**: property  
**Role**: Instance Property

A value indicating whether the connection prefers encrypted connections, unencrypted connections, or has no preference.

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
var encryptionPreference: MCEncryptionPreference { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, readonly) MCEncryptionPreference encryptionPreference;
```

*macOS*

```objc
@property (atomic, readonly) MCEncryptionPreference encryptionPreference;
```

#### Discussion

You set this value when you initialize the session object. It cannot be changed later. For possible values, see [`MCEncryptionPreference`](../mcencryptionpreference.md)

## See Also

### Creating a Session
- [convenience init(peer: MCPeerID)](./init%28peer%29.md)
  Creates a Multipeer Connectivity session.
- [init(peer: MCPeerID, securityIdentity: [Any]?, encryptionPreference: MCEncryptionPreference)](./init%28peer,securityidentity,encryptionpreference%29.md)
  Creates a Multipeer Connectivity session, providing security information.
- [var delegate: (any MCSessionDelegate)?](./delegate.md)
  The delegate object that handles session-related events.
- [var myPeerID: MCPeerID](./mypeerid.md)
  A local identifier that represents the device on which your app is currently running.
- [var securityIdentity: [Any]?](./securityidentity.md)
  The security identity of the local peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/encryptionpreference)*