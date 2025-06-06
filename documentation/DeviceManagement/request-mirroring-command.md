# Start AirPlay Mirroring

**Framework**: Device Management  
**Kind**: httpRequest

Prompt the user to share their screen using AirPlay Mirroring.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 10.10+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

MDM doesn’t support AirPlay destinations that have enabled Onscreen Codes. Provide either the `DestinationName` or the `DestinationDeviceID`. If you provide both values, MDM uses `DestinationDeviceID`.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS, Shared iPad |
| User Channel | macOS |
| Requires Supervision | - |
| Allowed in User Enrollment | iOS, macOS |
| Required Access Right | - |

##### Example Request and Response

## Topics

### Command and Response
- [object RequestMirroringCommand](requestmirroringcommand.md)
  The command to prompt the user to share their screen using AirPlay Mirroring.
- [object RequestMirroringResponse](requestmirroringresponse.md)
  A response from the device after it processes the command to prompt the user to share their screen using AirPlay Mirroring.

## Request Body

The command to prompt the user to share their screen using AirPlay Mirroring.

## See Also

- [Stop AirPlay Mirroring](stop-mirroring-command.md)
  Stop mirroring the display on another device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/request-mirroring-command)*