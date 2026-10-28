# User Configured

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Inform the device that it can continue past Setup Assistant and finish login.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Discussion

Refer to the following sections to determine supported channels and requirements.

### Command availability

|  |  |
| --- | --- |
| Device channel | iOS |
| User channel | N/A |
| Requires supervision | iOS |
| Allowed in user enrollment | N/A |
| Required access right | N/A |

## Topics

### Commands and responses
- [object UserConfiguredCommand](./userconfiguredcommand.md)
  The command to inform the device that it can continue past Setup Assistant and finish login.
- [object UserConfiguredResponse](./userconfiguredresponse.md)
  A response from the device after it processes the command to inform the device that it can continue past Setup Assistant and finish login.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm`

## Request Body

**Content-Type**: `application/x-apple-aspen-mdm`  
**Type**: `UserConfiguredCommand`

The request object the server returns for the User Configured Command.

## Responses

- `200` OK (`UserConfiguredResponse`, `application/xml`): The response object the system returns for the User Configured Command.

## See Also

### Device details
- [Device Information](./device-information-command.md)
  Get detailed information about a device.
- [Device Configured](./device-configured-command.md)
  Inform the device that it can allow the user to continue in Setup Assistant.
- [Restrictions](./restrictions-command.md)
  Get a list of restrictions on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/user-configured-command)*