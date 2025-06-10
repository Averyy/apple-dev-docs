# LOM Device Request

**Framework**: Device Management  
**Kind**: httpRequest

Send requests to a device using lights-out management (LOM).

**Availability**:
- macOS 11.0+

#### Discussion

This command requires the `DeviceLockAndRemovePasscode` access right, [`LightsOutManagementLOM`](lightsoutmanagementlom.md) configuration and is available in macOS 11 and later on [`supported macOS devices`](https://developer.apple.comhttps://support.apple.com/guide/deployment/lights-out-management-payload-settings-dep580cf25bc/web).

`DeviceDNSName` is the `CommonName` in the Identity issued on the client certificate from [`LightsOutManagementLOM`](lightsoutmanagementlom.md). [`LOMSetupRequestResponse`](lomsetuprequestresponse.md) returns `PrimaryIPv6AddressList` and `SecondaryIPv6AddressList` after a successful deployment of Lights Out management configuration payload and subsequent [`LOMSetupRequestCommand`](lomsetuprequestcommand.md).

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
- [object LOMDeviceRequestCommand](lomdevicerequestcommand.md)
  The command to send requests to a device using lights-out management (LOM).
- [object LOMDeviceRequestResponse](lomdevicerequestresponse.md)
  A response from the device after it processes the command to send requests to a device using lights-out management (LOM).

## Request Body

The request object the server returns for the LOM Device Request Command.

## See Also

- [LOM Setup Request](lom-setup-request-command.md)
  Get information from a device to set up lights-out management (LOM).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/lom-device-request-command)*