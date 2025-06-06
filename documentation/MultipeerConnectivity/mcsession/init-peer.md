# init(peer:)

**Framework**: Multipeer Connectivity  
**Kind**: init

Creates a Multipeer Connectivity session.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(peer myPeerID: MCPeerID)
```

#### Return Value

The initialized session object, or `nil` if an error occurs.

#### Discussion

This method is equivalent to calling [`init(peer:securityIdentity:encryptionPreference:)`](mcsession/init(peer:securityidentity:encryptionpreference:).md) with a `nil` identity and an encryption setting that varies based on which version of the SDK was used to link the application. On apps linked on or after iOS 9, the encryption is set to [`MCEncryptionPreference.required`](mcencryptionpreference/required.md). On apps linked prior to iOS 9, the encryption is set to [`MCEncryptionPreference.optional`](mcencryptionpreference/optional.md).

This method throws an exception if the provided peer ID object is invalid or `nil`.

For more information, see [`Initiating a Session`](mcsession#Initiating-a-Session.md).

## Parameters

- `myPeerID`: A local identifier that represents the device on which your app is currently running.

## See Also

- [init(peer: MCPeerID, securityIdentity: [Any]?, encryptionPreference: MCEncryptionPreference)](mcsession/init(peer:securityidentity:encryptionpreference:).md)
  Creates a Multipeer Connectivity session, providing security information.
- [var delegate: (any MCSessionDelegate)?](mcsession/delegate.md)
  The delegate object that handles session-related events.
- [var encryptionPreference: MCEncryptionPreference](mcsession/encryptionpreference.md)
  A value indicating whether the connection prefers encrypted connections, unencrypted connections, or has no preference.
- [var myPeerID: MCPeerID](mcsession/mypeerid.md)
  A local identifier that represents the device on which your app is currently running.
- [var securityIdentity: [Any]?](mcsession/securityidentity.md)
  The security identity of the local peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/init(peer:))*