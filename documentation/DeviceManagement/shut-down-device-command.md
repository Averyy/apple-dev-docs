# Shut Down Device

**Framework**: Device Management  
**Kind**: httpRequest

Remotely and immediately shut down a device.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- macOS 10.13+

#### Discussion

A passcode-locked iOS device doesn’t rejoin a Wi-Fi network after restarting, so it may not be able to communicate with the server.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad |
| User channel | NA |
| Requires supervision | iOS, macOS |
| Allowed in user enrollment | NA |
| Required access right | AllowPasscodeRemovalAndLock |

##### Example Request and Response

## Topics

### Commands and responses
- [object ShutDownDeviceCommand](shutdowndevicecommand.md)
  The command to remotely and immediately shut down a device.
- [object ShutDownDeviceResponse](shutdowndeviceresponse.md)
  A response from the device after it processes the command to remotely and immediately shut down a device.

## Request Body

The request object the server returns for the Shut Down Device Command.

## See Also

- [Erase Device](erase-device-command.md)
  Remotely and immediately erase a device.
- [Device Lock](device-lock-command.md)
  Remotely and immediately lock a device.
- [Restart Device](restart-device-command.md)
  Remotely and immediately restart a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/shut-down-device-command)*