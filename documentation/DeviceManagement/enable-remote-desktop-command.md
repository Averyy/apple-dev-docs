# Enable Remote Desktop

**Framework**: Device Management  
**Kind**: httpRequest

Enable Remote Desktop on a device.

**Availability**:
- macOS 10.14.4+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This command enables the following capabilities on the device:

- Remote Desktop with the All Users access
- The ability to receive remote events
- The Observe, Control, and Show being Observed options

All other options remain unchanged.

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
- [object EnableRemoteDesktopCommand](enableremotedesktopcommand.md)
  The command to enable Remote Desktop on a device.
- [object EnableRemoteDesktopResponse](enableremotedesktopresponse.md)
  A response from the device after it processes the command to enable Remote Desktop on a device.

## Request Body

The command to enable Remote Desktop on a device.

## See Also

- [Disable Remote Desktop](disable-remote-desktop-command.md)
  Disable Remote Desktop on a device.
- [Configure Settings](settings-command.md)
  Configure settings on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/enable-remote-desktop-command)*