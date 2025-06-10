# Check-in

**Framework**: Device Management

Authenticate devices and maintain push tokens with these commands.

#### Overview

The MDM check-in protocol validates a deviceʼs eligibility for MDM enrollment and informs the server that a deviceʼs push token has been updated.

When the MDM payload is installed, the device initiates communication with the check-in server. The device validates the TLS certificate of the server, then uses the identity specified in its MDM payload as the client authentication certificate for the connection.

If a check-in server URL is provided in the MDM payload, the check-in protocol communicates with that check-in server. If no check-in server URL is provided, the main MDM server URL is used instead.

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
### Declarative Management
- [Declarative Management](declarative-management.md)
  Sends declarative management requests to the server.
- [Get Server Supported Declarations](declaration-items.md)
  Get a list of the declarations available on the server.
- [Get the Device Status](status.md)
  The request for getting the status of a device.
- [Get the Device Token](tokens.md)
  The request for sending the device token details.

## See Also

- [Implementing Device Management](implementing-device-management.md)
  Set up an MDM server and send commands to managed devices.
- [Commands and Queries](commands-and-queries.md)
  Manage the configuration and behavior of your devices.
- [Account-driven enrollment](account-driven-enrollment.md)
  Authenticate devices using a user identity-focused workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/check-in)*