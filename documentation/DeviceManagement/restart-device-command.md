# Restart a Device

**Framework**: Device Management  
**Kind**: httpRequest

Remotely and immediately restart a device.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- macOS 10.13+
- tvOS 10.2+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

A passcode-locked iOS device doesn’t rejoin a Wi-Fi network after restarting, so it may not be able to communicate with the server.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS, Shared iPad, tvOS |
| User Channel | - |
| Requires Supervision | iOS, tvOS |
| Allowed in User Enrollment | - |
| Required Access Right | AllowPasscodeRemovalAndLock |

##### Example Request and Response

## Topics

### Command and Response
- [object RestartDeviceCommand](restartdevicecommand.md)
  The command to restart a device.
- [object RestartDeviceResponse](restartdeviceresponse.md)
  A response from the device after it processes the command to restart.

## Request Body

The command to restart a device.

## See Also

- [Erase a Device](erase-device-command.md)
  Remotely and immediately erase a device.
- [Lock a Device](device-lock-command.md)
  Remotely and immediately lock a device.
- [Shut Down a Device](shut-down-device-command.md)
  Remotely and immediately shut down a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/restart-device-command)*