# Shut Down a Device

**Framework**: Device Management  
**Kind**: httpRequest

Remotely and immediately shut down a device.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- macOS 10.13+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

A passcode-locked iOS device doesn’t rejoin a Wi-Fi network after restarting, so it may not be able to communicate with the server.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS, Shared iPad |
| User Channel | - |
| Requires Supervision | iOS |
| Allowed in User Enrollment | - |
| Required Access Right | AllowPasscodeRemovalAndLock |

##### Example Request and Response

## Topics

### Command and Response
- [object ShutDownDeviceCommand](shutdowndevicecommand.md)
  The command to shut down a device.
- [object ShutDownDeviceResponse](shutdowndeviceresponse.md)
  A response from the device after it processes the command to shut down.

## Request Body

The command to shut down a device.

## See Also

- [Erase a Device](erase-device-command.md)
  Remotely and immediately erase a device.
- [Lock a Device](device-lock-command.md)
  Remotely and immediately lock a device.
- [Restart a Device](restart-device-command.md)
  Remotely and immediately restart a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/shut-down-device-command)*