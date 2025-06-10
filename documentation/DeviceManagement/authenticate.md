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

## Mentions

- [Implementing the simple authentication account-driven enrollment flow](implementing-the-simple-authentication-user-enrollment-flow.md)

#### Discussion

On success, the server needs to respond with a `200 OK` status. Don’t assume that the device has installed the MDM payload at this time because other payloads in the profile may still fail to install. When the device successfully installs the MDM payload, it sends a [`Token Update`](token-update.md) message.

##### Check in Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | NA |
| Requires supervision | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |

## Topics

### Requests
- [object AuthenticateRequest](authenticaterequest.md)
  The authenticate request details.

## Request Body

The request object the system sends for the `Authenticate` request.

## See Also

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
- [Set Bootstrap Token](set-bootstrap-token.md)
  Sends the bootstrap token to the server.
- [Return To Service](return-to-service.md)
  Gets the return-to-service configuration from the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/authenticate)*