# Get Bootstrap Token

**Framework**: Device Management  
**Kind**: httpRequest

Gets the bootstrap token.

**Availability**:
- macOS 10.15+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This command returns the bootstrap token data if it was previously set and the feature is enabled by the server.

If no bootstrap token is available, the server should return empty or no data and no error.

It requires a Device Enrollment Program enrolled client, or on macOS 11 and later, a supervised device.

## Topics

### Request and Response
- [object GetBootstrapTokenRequest](getbootstraptokenrequest.md)
  The request object used to get the bootstrap token.
- [object GetBootstrapTokenResponse](getbootstraptokenresponse.md)
  The response that contains the bootstrap token.

## Request Body

The request object the app uses to get the bootstrap token.

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
- [Set Bootstrap Token](set-bootstrap-token.md)
  Sets the bootstrap token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-bootstrap-token)*