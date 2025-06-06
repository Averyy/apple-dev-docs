# Erase a Device

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
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This command allows the server to immediately erase a device, even a locked device, without warning the user. The device sends a response to the server, but it doesn’t retry if it isn’t successful the first time.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS, Shared iPad, tvOS, watchOS |
| User Channel | - |
| Requires Supervision | - |
| Allowed in User Enrollment | - |
| Required Access Right | AllowDeviceErase |

##### Example Request and Response

## Topics

### Command and Response
- [object EraseDeviceCommand](erasedevicecommand.md)
  The command to erase a device.
- [object EraseDeviceResponse](erasedeviceresponse.md)
  A response from the device after it processes the command to erase.

## Request Body

The command to erase a device.

## See Also

- [Lock a Device](device-lock-command.md)
  Remotely and immediately lock a device.
- [Restart a Device](restart-device-command.md)
  Remotely and immediately restart a device.
- [Shut Down a Device](shut-down-device-command.md)
  Remotely and immediately shut down a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/erase-device-command)*