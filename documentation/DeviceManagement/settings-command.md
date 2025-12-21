# Settings

**Framework**: Device Management  
**Kind**: httpRequest

Configure settings on a device.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+

## Mentions

- [Returning a managed device to service](returning-a-managed-device-to-service.md)

#### Discussion

Users may be able to change the settings later if a profile isn’t set to restrict such changes.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | macOS, Shared iPad |
| Requires supervision | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Required access right | AllowSettings |

##### Example Request and Response Devicename

## Topics

### Commands and responses
- [object SettingsCommand](settingscommand.md)
  The command to configure settings on a device.
- [object SettingsResponse](settingsresponse.md)
  A response from the device after it processes the command to configure settings on a device.

## Request Body

The request object the server returns for the Settings Command.

## See Also

- [Disable Remote Desktop](disable-remote-desktop-command.md)
  Disable Remote Desktop on a device.
- [Enable Remote Desktop](enable-remote-desktop-command.md)
  Enable Remote Desktop on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/settings-command)*