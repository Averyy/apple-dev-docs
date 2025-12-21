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

## Mentions

- [Migrating managed devices](migrating-managed-devices.md)

#### Discussion

The system sends this message on a best-effort basis. If the system can’t send the message while removing the MDM profile, it removes the profile and doesn’t resend the message.

On success, the server needs to respond with a `200 OK` status.

##### Check in Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | NA |
| Requires supervision | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |

## Topics

### Requests
- [object CheckOutRequest](checkoutrequest.md)
  The check out request details.

## Request Body

The request object the system sends for the `CheckOut` request.

## See Also

- [Authenticate](authenticate.md)
  Authenticates a user during MDM payload installation.
- [User Authenticate](user-authenticate.md)
  Authenticates a user with a two-step authentication protocol.
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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/check-out)*