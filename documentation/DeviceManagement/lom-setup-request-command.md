# LOM Setup Request

**Framework**: Device Management  
**Kind**: httpRequest

Get information from a device to set up lights-out management (LOM).

**Availability**:
- macOS 11.0+

#### Discussion

This command requires the `DeviceLockAndRemovePasscode` access right, [`LightsOutManagementLOM`](lightsoutmanagementlom.md) configuration and is available in macOS 11 and later on [`supported macOS devices`](https://developer.apple.comhttps://support.apple.com/guide/deployment/lights-out-management-payload-settings-dep580cf25bc/web).

##### Command Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
| Requires supervision | macOS |
| Allowed in user enrollment | NA |
| Required access right | DeviceLockAndRemovePasscode |

##### Example Request and Response

## Topics

### Commands and responses
- [object LOMSetupRequestCommand](lomsetuprequestcommand.md)
  The command to get information from a device to set up lights-out management (LOM).
- [object LOMSetupRequestResponse](lomsetuprequestresponse.md)
  A response from the device after it processes the command to get information from a device to set up lights-out management (LOM).

## Request Body

The request object the server returns for the LOM Setup Request Command.

## See Also

- [LOM Device Request](lom-device-request-command.md)
  Send requests to a device using lights-out management (LOM).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/lom-setup-request-command)*