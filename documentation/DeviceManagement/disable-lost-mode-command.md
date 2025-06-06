# Disable Lost Mode

**Framework**: Device Management  
**Kind**: httpRequest

Take the device out of Lost Mode.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

A device responds with error code `12067` if it isn’t in Lost Mode, or error code `12069` if the request to disable Lost Mode failed. While in Lost Mode, a device responds to invalid commands with error code `12078`.

Erasing a device also disables Lost Mode. To reenable Lost Mode, the MDM server stores the device’s Lost Mode state before erasing it, and restores that state if the device enrolls again.

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
- [object DisableLostModeCommand](disablelostmodecommand.md)
  The command to disable Lost Mode.
- [object DisableLostModeResponse](disablelostmoderesponse.md)
  A response from the device after it processes the command to disable Lost Mode.

## Request Body

The command to disable Lost Mode.

## See Also

- [Enable Lost Mode](enable-lost-mode-command.md)
  Enable Lost Mode on a device, which provides a message and phone number on the Lock screen.
- [Get the Location of a Device](device-location-command.md)
  Request the location of a device when in Lost Mode.
- [Play the Lost Mode Sound](play-lost-mode-sound-command.md)
  Play the Lost Mode sound on a device that’s in Lost Mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/disable-lost-mode-command)*