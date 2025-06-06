# Enable Lost Mode

**Framework**: Device Management  
**Kind**: httpRequest

Enable Lost Mode on a device, which provides a message and phone number on the Lock screen.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

While in Lost Mode, a device responds to invalid commands with error code `12078`.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | iOS, Shared iPad |
| User Channel | - |
| Requires Supervision | iOS |
| Allowed in User Enrollment | - |
| Required Access Right | - |

##### Example Request and Response

## Topics

### Command and Response
- [object EnableLostModeCommand](enablelostmodecommand.md)
  The command to enable Lost Mode.
- [object EnableLostModeResponse](enablelostmoderesponse.md)
  A response from the device after it processes the command to enable Lost Mode.

## Request Body

The command to enable Lost Mode.

## See Also

- [Get the Location of a Device](device-location-command.md)
  Request the location of a device when in Lost Mode.
- [Play the Lost Mode Sound](play-lost-mode-sound-command.md)
  Play the Lost Mode sound on a device that’s in Lost Mode.
- [Disable Lost Mode](disable-lost-mode-command.md)
  Take the device out of Lost Mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/enable-lost-mode-command)*