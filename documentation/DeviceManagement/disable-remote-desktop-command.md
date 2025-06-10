# Disable Remote Desktop

**Framework**: Device Management  
**Kind**: httpRequest

Disable Remote Desktop on a device.

**Availability**:
- macOS 10.14.4+

#### Discussion

This command prevents any further event processing. It removes any `PostEvent` Transparency Consent and Control (TCC) ability, unless the device already has an installed TCC configuration profile with that ability enabled.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
| Requires supervision | macOS |
| Allowed in user enrollment | NA |
| Required access right |  |

##### Example Request and Response

## Topics

### Commands and responses
- [object DisableRemoteDesktopCommand](disableremotedesktopcommand.md)
  The command to disable Remote Desktop on a device.
- [object DisableRemoteDesktopResponse](disableremotedesktopresponse.md)
  A response from the device after it processes the command to disable Remote Desktop on a device.

## Request Body

The request object the server returns for the Disable Remote Desktop Command.

## See Also

- [Enable Remote Desktop](enable-remote-desktop-command.md)
  Enable Remote Desktop on a device.
- [Settings](settings-command.md)
  Configure settings on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/disable-remote-desktop-command)*