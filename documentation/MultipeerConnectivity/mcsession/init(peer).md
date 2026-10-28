# init(peer:)

**Framework**: Multipeer Connectivity  
**Kind**: init  
**Role**: Initializer

Creates a Multipeer Connectivity session.

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
convenience init(peer myPeerID: MCPeerID)
```

```objc
- (instancetype) initWithPeer:(MCPeerID *) myPeerID;
```

## Return Value

The initialized session object, or `nil` if an error occurs.

## Discussion

This method is equivalent to calling [`init(peer:securityIdentity:encryptionPreference:)`](./init%28peer,securityidentity,encryptionpreference%29.md) with a `nil` identity and an encryption setting that varies based on which version of the SDK was used to link the application. On apps linked on or after iOS 9, the encryption is set to [`MCEncryptionPreference.required`](../mcencryptionpreference/required.md). On apps linked prior to iOS 9, the encryption is set to [`MCEncryptionPreference.optional`](../mcencryptionpreference/optional.md).

This method throws an exception if the provided peer ID object is invalid or `nil`.

For more information, see [Initiating a Session](../mcsession.md#Initiating-a-Session).

## Parameters

- `myPeerID`: A local identifier that represents the device on which your app is currently running.

## See Also

### Creating a Session
- [init(peer: MCPeerID, securityIdentity: [Any]?, encryptionPreference: MCEncryptionPreference)](./init%28peer,securityidentity,encryptionpreference%29.md)
  Creates a Multipeer Connectivity session, providing security information.
- [var delegate: (any MCSessionDelegate)?](./delegate.md)
  The delegate object that handles session-related events.
- [var encryptionPreference: MCEncryptionPreference](./encryptionpreference.md)
  A value indicating whether the connection prefers encrypted connections, unencrypted connections, or has no preference.
- [var myPeerID: MCPeerID](./mypeerid.md)
  A local identifier that represents the device on which your app is currently running.
- [var securityIdentity: [Any]?](./securityidentity.md)
  The security identity of the local peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/init(peer:))*