# Enable Remote Desktop

**Framework**: Device Management  
**Kind**: httpRequest

Enable Remote Desktop on a device.

**Availability**:
- macOS 10.14.4+

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
| Device channel | macOS |
| User channel | NA |
| Requires supervision | macOS |
| Allowed in user enrollment | NA |
| Required access right |  |

##### Example Request and Response

## Topics

### Commands and responses
- [object EnableRemoteDesktopCommand](enableremotedesktopcommand.md)
  The command to enable Remote Desktop on a device.
- [object EnableRemoteDesktopResponse](enableremotedesktopresponse.md)
  A response from the device after it processes the command to enable Remote Desktop on a device.

## Request Body

The request object the server returns for the Enable Remote Desktop Command.

## See Also

- [Disable Remote Desktop](disable-remote-desktop-command.md)
  Disable Remote Desktop on a device.
- [Settings](settings-command.md)
  Configure settings on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/enable-remote-desktop-command)*