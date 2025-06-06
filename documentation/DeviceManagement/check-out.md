# Check Out

**Framework**: Device Management  
**Kind**: httpRequest

Responds to the removal of the MDM enrollment profile from a device.

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

This message is sent on a best-effort basis. If the message cannot be sent while the profile is being removed, the MDM profile will be removed, and the message will not be resent.

On success, the server must respond with a `200 OK` status.

## Topics

### Request
- [object CheckOutRequest](checkoutrequest.md)
  The Check Out Request details.

## Request Body

The request object for check out.

## See Also

- [Authenticate](authenticate.md)
  Authenticates a user during MDM payload installation.
- [UserAuthenticate](userauthenticate.md)
  Authenticates a user with a two-step authentication protocol.
- [Get Token](get-token.md)
  Check-in protocol get-token data.
- [Token Update](token-update.md)
  Updates the token for a device on the server.
- [Get Bootstrap Token](get-bootstrap-token.md)
  Gets the bootstrap token.
- [Set Bootstrap Token](set-bootstrap-token.md)
  Sets the bootstrap token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/check-out)*