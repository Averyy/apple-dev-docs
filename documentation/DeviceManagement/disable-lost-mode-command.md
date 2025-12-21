# Disable Lost Mode

**Framework**: Device Management  
**Kind**: httpRequest

Take the device out of Lost Mode.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+

#### Discussion

A device responds with error codes:

- `12067`: If it isn’t in Lost Mode.
- `12069`: If the request to disable Lost Mode failed.
- `12078`: If the command is invalid while in Lost Mode.

Erasing a device also disables Lost Mode. To reenable Lost Mode, the MDM server needs to store the device’s Lost Mode state before erasing it, and restore that state if the device enrolls again.

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
- [object DisableLostModeCommand](disablelostmodecommand.md)
  The command to take the device out of Lost Mode.
- [object DisableLostModeResponse](disablelostmoderesponse.md)
  A response from the device after it processes the command to take the device out of Lost Mode.

## Request Body

The request object the server returns for the Disable Lost Mode Command.

## See Also

- [Enable Lost Mode](enable-lost-mode-command.md)
  Enable Lost Mode on a device, which provides a message and phone number on the Lock Screen.
- [Device Location](device-location-command.md)
  Request the location of a device when in Lost Mode.
- [Play Lost Mode Sound](play-lost-mode-sound-command.md)
  Play the Lost Mode sound on a device that’s in Lost Mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/disable-lost-mode-command)*