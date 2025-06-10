# Set Bootstrap Token

**Framework**: Device Management  
**Kind**: httpRequest

Sends the bootstrap token to the server.

**Availability**:
- macOS 10.15+

#### Discussion

A server that supports this request needs to include a `com.apple.mdm.bootstraptoken` value in the `ServerCapabilities` key of the MDM profile payload to enroll the device.

This request changes or clears a device’s bootstrap token data that the server stores.

It requires a device using Automated Device Enrollment, or a supervised device in macOS 11 and later.

##### Check in Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
| Requires supervision | macOS |
| Allowed in user enrollment | NA |

## Topics

### Requests
- [object SetBootstrapTokenRequest](setbootstraptokenrequest.md)
  The set bootstrap token request details.

## Request Body

The request object the system sends for the `SetBootstrapToken` request.

## See Also

- [Authenticate](authenticate.md)
  Authenticates a user during MDM payload installation.
- [User Authenticate](user-authenticate.md)
  Authenticates a user with a two-step authentication protocol.
- [Check Out](check-out.md)
  Responds to the removal of the MDM enrollment profile from a device.
- [Get Token](get-token.md)
  Gets a token from the server.
- [Token Update](token-update.md)
  Updates the token for a device on the server.
- [Get Bootstrap Token](get-bootstrap-token.md)
  Gets the bootstrap token from the server.
- [Return To Service](return-to-service.md)
  Gets the return-to-service configuration from the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/set-bootstrap-token)*