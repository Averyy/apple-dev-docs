# Erase Device

**Framework**: Device Management  
**Kind**: httpRequest

Remotely and immediately erase a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

#### Discussion

This command allows the server to immediately erase a device, even a locked device, without warning the user. The device sends a response to the server, but it doesn’t retry if it isn’t successful the first time.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | NA |
| Requires supervision | macOS |
| Allowed in user enrollment | NA |
| Required access right | AllowDeviceErase |

##### Example Request and Response

## Topics

### Commands and responses
- [object EraseDeviceCommand](erasedevicecommand.md)
  The command to remotely and immediately erase a device.
- [object EraseDeviceResponse](erasedeviceresponse.md)
  A response from the device after it processes the command to remotely and immediately erase a device.

## Request Body

The request object the server returns for the Erase Device Command.

## See Also

- [Device Lock](device-lock-command.md)
  Remotely and immediately lock a device.
- [Restart Device](restart-device-command.md)
  Remotely and immediately restart a device.
- [Shut Down Device](shut-down-device-command.md)
  Remotely and immediately shut down a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/erase-device-command)*