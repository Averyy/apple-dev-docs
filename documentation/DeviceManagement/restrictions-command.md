# List the Installed Restrictions

**Framework**: Device Management  
**Kind**: httpRequest

Get a list of restrictions on the device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Query Availability

|  |  |
| --- | --- |
| Device Channel | iOS, Shared iPad, tvOS, watchOS |
| User Channel | Shared iPad |
| Requires Supervision | - |
| Allowed in User Enrollment | - |
| Required Access Right | AllowQueryRestrictions |

##### Example Request and Response

## Topics

### Command and Response
- [object RestrictionsCommand](restrictionscommand.md)
  The command to get a list of restrictions on a device.
- [object RestrictionsResponse](restrictionsresponse.md)
  A response from the device after it processes the command to get a list of restrictions.

## Request Body

The command to get a list of restrictions on a device.

## See Also

- [List the Installed Apps](installed-application-list-command.md)
  Get a list of the installed apps on a device.
- [Get Device Information](device-information-command.md)
  Get detailed information about a device.
- [Release Device from Await Configuration](device-configured-command.md)
  Inform the device that it can allow the user to continue in Setup Assistant.
- [User Configured Command](user-configured-command.md)
  Informs the device that it can continue past Setup Assistant and finish login.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/restrictions-command)*