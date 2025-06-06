# Set Bootstrap Token

**Framework**: Device Management  
**Kind**: httpRequest

Sets the bootstrap token.

**Availability**:
- macOS 10.15+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This command changes or clears the bootstrap token data for the device.

It requires a Device Enrollment Program enrolled client, or on macOS 11 and later, a supervised device.

## Topics

### Request
- [object SetBootstrapTokenRequest](setbootstraptokenrequest.md)
  The request object used to set the bootstrap token.

## Request Body

The request object used to set the bootstrap token.

## See Also

- [Authenticate](authenticate.md)
  Authenticates a user during MDM payload installation.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/set-bootstrap-token)*