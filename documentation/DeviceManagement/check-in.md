# Check-in

**Framework**: Device Management

Authenticate devices and maintain push tokens.

#### Overview

The Mobile Device Management (MDM) check-in protocol validates a deviceʼs eligibility for enrollment and informs the device management service that a deviceʼs push token has been updated.

After installing the MDM payload, the device initiates communication with the check-in service. The device validates the TLS certificate of the service, then uses the identity specified in its MDM payload as the client authentication certificate for the connection.

If the MDM payload includes a check-in URL, the check-in protocol communicates with that check-in service. If it doesn’t provide a check-in URL, the device uses the main device management service URL instead.

## Topics

### Commands
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
- [Set Bootstrap Token](set-bootstrap-token.md)
  Sends the bootstrap token to the server.
- [Return To Service](return-to-service.md)
  Gets the return-to-service configuration from the server.
### Declarative management
- [Declarative Management](declarative-management.md)
  Sends declarative management requests to the server.
- [Get Server Supported Declarations](declaration-items.md)
  Get a list of the declarations available on the server.
- [Get the Device Status](status.md)
  The request for getting the status of a device.
- [Get the Device Token](tokens.md)
  The request for sending the device token details.

## See Also

- [Commands and queries](commands-and-queries.md)
  Remotely execute management commands and queries on managed devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/check-in)*