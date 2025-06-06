# LOM Setup Request Command

**Framework**: Device Management  
**Kind**: httpRequest

Get information from a device to set up lights-out management (LOM).

**Availability**:
- macOS 11.0+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This command requires the `DeviceLockAndRemovePasscode` access right, [`LightsOutManagementLOM`](lightsoutmanagementlom.md) configuration and is available in macOS 11 and later on [`supported macOS devices`](https://developer.apple.comhttps://support.apple.com/guide/deployment/lights-out-management-payload-settings-dep580cf25bc/web).

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | macOS |
| User Channel | - |
| Requires Supervision | - |
| Allowed in User Enrollment | - |
| Required Access Right | DeviceLockAndRemovePasscode |

##### Example Request and Response

## Topics

### Command and Response
- [object LOMSetupRequestCommand](lomsetuprequestcommand.md)
  The command to get information from a device to set up lights-out management (LOM).
- [object LOMSetupRequestResponse](lomsetuprequestresponse.md)
  A response from the device after it processes the command to get setup information for lights-out management (LOM).

## Request Body

The command to get information from a device to set up lights-out management (LOM).

## See Also

- [LOM Device Request Command](lom-device-request-command.md)
  Send requests to a device using lights-out management (LOM).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/lom-setup-request-command)*