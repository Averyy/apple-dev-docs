# Get Bootstrap Token

**Framework**: Device Management  
**Kind**: httpRequest

Gets the bootstrap token from the server.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 10.15+
- visionOS 26.0+

#### Discussion

A server that supports this request needs to include a `com.apple.mdm.bootstraptoken` value in the `ServerCapabilities` key of the MDM profile payload to enroll the device.

This request returns the device’s bootstrap token data that the server stores.

If a bootstrap token isn’t available, the server returns a success response with either a zero-length value for the `BootstrapToken` key or omits the key.

Requires a device enrolled using Automated Device Enrollment.

##### Check in Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, visionOS |
| User channel | NA |
| Requires supervision | iOS, macOS, visionOS |
| Allowed in user enrollment | NA |

## Topics

### Requests and responses
- [object GetBootstrapTokenRequest](getbootstraptokenrequest.md)
  The get bootstrap token request details.
- [object GetBootstrapTokenResponse](getbootstraptokenresponse.md)
  The get bootstrap token response details.

## Request Body

The request object the system sends for the `GetBootstrapToken` request.

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
- [Set Bootstrap Token](set-bootstrap-token.md)
  Sends the bootstrap token to the server.
- [Return To Service](return-to-service.md)
  Gets the return-to-service configuration from the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-bootstrap-token)*