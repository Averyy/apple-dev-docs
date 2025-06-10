# Device Location

**Framework**: Device Management  
**Kind**: httpRequest

Request the location of a device when in Lost Mode.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+

#### Discussion

A device responds with error code `12067` if it isn’t in Lost Mode, or error code `12068` if its location is unknown. While in Lost Mode, a device responds to invalid commands with error code `12078`.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, Shared iPad |
| User channel | NA |
| Requires supervision | iOS |
| Allowed in user enrollment | NA |
| Required access right | NA |

##### Example Request and Response

## Topics

### Commands and responses
- [object DeviceLocationCommand](devicelocationcommand.md)
  The command to request the location of a device when in Lost Mode.
- [object DeviceLocationResponse](devicelocationresponse.md)
  A response from the device after it processes the command to request the location of a device when in Lost Mode.

## Request Body

The request object the server returns for the Device Location Command.

## See Also

- [Enable Lost Mode](enable-lost-mode-command.md)
  Enable Lost Mode on a device, which provides a message and phone number on the Lock Screen.
- [Play Lost Mode Sound](play-lost-mode-sound-command.md)
  Play the Lost Mode sound on a device that’s in Lost Mode.
- [Disable Lost Mode](disable-lost-mode-command.md)
  Take the device out of Lost Mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/device-location-command)*