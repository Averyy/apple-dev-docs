# Stop AirPlay Mirroring

**Framework**: Device Management  
**Kind**: httpRequest

Stop mirroring the display on another device.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 10.10+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS, Shared iPad |
| User Channel | - |
| Requires Supervision | iOS |
| Allowed in User Enrollment | - |
| Required Access Right | - |

##### Example Request and Response

## Topics

### Command and Response
- [object StopMirroringCommand](stopmirroringcommand.md)
  The command to stop mirroring the display on another device.
- [object StopMirroringResponse](stopmirroringresponse.md)
  A response from the device after it processes the command to stop mirroring the display on another device.

## Request Body

The command to stop mirroring the display on another device.

## See Also

- [Start AirPlay Mirroring](request-mirroring-command.md)
  Prompt the user to share their screen using AirPlay Mirroring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/stop-mirroring-command)*