# Authenticate

**Framework**: Device Management  
**Kind**: httpRequest

Authenticates a user during MDM payload installation.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

On success, the server must respond with a `200 OK` status. The server shouldn’t assume that the device has installed the MDM payload at this time, as other payloads in the profile may still fail to install. When the device has successfully installed the MDM payload, it sends a [`Token Update`](token-update.md) message.

## Topics

### Request
- [object AuthenticateRequest](authenticaterequest.md)
  The Authenticate Request details.

## Request Body

The request object for authentication.

## See Also

- [UserAuthenticate](userauthenticate.md)
  Authenticates a user with a two-step authentication protocol.
- [Check Out](check-out.md)
  Responds to the removal of the MDM enrollment profile from a device.
- [Get Token](get-token.md)
  Check-in protocol get-token data.
- [Token Update](token-update.md)
  Updates the token for a device on the server.
- [Get Bootstrap Token](get-bootstrap-token.md)
  Gets the bootstrap token.
- [Set Bootstrap Token](set-bootstrap-token.md)
  Sets the bootstrap token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/authenticate)*