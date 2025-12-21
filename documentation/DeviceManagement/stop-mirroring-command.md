# Stop Mirroring

**Framework**: Device Management  
**Kind**: httpRequest

Stop mirroring the display to another device.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 10.10+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad |
| User channel | NA |
| Requires supervision | iOS, macOS |
| Allowed in user enrollment | NA |
| Required access right | NA |

##### Example Request and Response

## Topics

### Commands and responses
- [object StopMirroringCommand](stopmirroringcommand.md)
  The command to stop mirroring the display to another device.
- [object StopMirroringResponse](stopmirroringresponse.md)
  A response from the device after it processes the command to stop mirroring the display to another device.

## Request Body

The request object the server returns for the Stop Mirroring Command.

## See Also

- [Request Mirroring](request-mirroring-command.md)
  Prompt the user to share their screen using AirPlay Mirroring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/stop-mirroring-command)*