# Disable Remote Desktop

**Framework**: Device Management  
**Kind**: httpRequest

Disable Remote Desktop on a device.

**Availability**:
- macOS 10.14.4+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This command prevents any further event processing. It removes any `PostEvent` Transparency Consent and Control (TCC) ability, unless the device already has an installed TCC configuration profile with that ability enabled.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | macOS |
| User Channel | - |
| Requires Supervision | macOS |
| Allowed in User Enrollment | - |
| Required Access Right | - |

##### Example Request and Response

## Topics

### Command and Response
- [object DisableRemoteDesktopCommand](disableremotedesktopcommand.md)
  The command to disable Remote Desktop on a device.
- [object DisableRemoteDesktopResponse](disableremotedesktopresponse.md)
  A response from the device after it processes the command to disable Remote Desktop.

## Request Body

The command to disable Remote Desktop on a device.

## See Also

- [Enable Remote Desktop](enable-remote-desktop-command.md)
  Enable Remote Desktop on a device.
- [Configure Settings](settings-command.md)
  Configure settings on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/disable-remote-desktop-command)*