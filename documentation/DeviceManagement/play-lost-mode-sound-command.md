# Play the Lost Mode Sound

**Framework**: Device Management  
**Kind**: httpRequest

Play the Lost Mode sound on a device that’s in Lost Mode.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

A device responds with error code `12067` if it isn’t in Lost Mode. While in Lost Mode, a device responds to invalid commands with error code `12078`.

The sound plays until the server disables Lost Mode or the user disables the sound on the device.

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
- [object PlayLostModeSoundCommand](playlostmodesoundcommand.md)
  The command to play the Lost Mode sound.
- [object PlayLostModeSoundResponse](playlostmodesoundresponse.md)
  A response from the device in Lost Mode after it processes the command to play the Lost Mode sound.

## Request Body

The command to play the Lost Mode sound.

## See Also

- [Enable Lost Mode](enable-lost-mode-command.md)
  Enable Lost Mode on a device, which provides a message and phone number on the Lock screen.
- [Get the Location of a Device](device-location-command.md)
  Request the location of a device when in Lost Mode.
- [Disable Lost Mode](disable-lost-mode-command.md)
  Take the device out of Lost Mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/play-lost-mode-sound-command)*