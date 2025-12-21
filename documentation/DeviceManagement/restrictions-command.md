# Restrictions

**Framework**: Device Management  
**Kind**: httpRequest

Get a list of restrictions on the device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | Shared iPad |
| Requires supervision | NA |
| Allowed in user enrollment | NA |
| Required access right | AllowQueryRestrictions |

##### Example Request and Response

## Topics

### Commands and responses
- [object RestrictionsCommand](restrictionscommand.md)
  The command to get a list of restrictions on the device.
- [object RestrictionsResponse](restrictionsresponse.md)
  A response from the device after it processes the command to get a list of restrictions on the device.

## Request Body

The request object the server returns for the Restrictions Command.

## See Also

- [Device Information](device-information-command.md)
  Get detailed information about a device.
- [Device Configured](device-configured-command.md)
  Inform the device that it can allow the user to continue in Setup Assistant.
- [User Configured](user-configured-command.md)
  Inform the device that it can continue past Setup Assistant and finish login.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/restrictions-command)*