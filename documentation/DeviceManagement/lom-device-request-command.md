# LOM Device Request Command

**Framework**: Device Management  
**Kind**: httpRequest

Send requests to a device using lights-out management (LOM).

**Availability**:
- macOS 11.0+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This command requires the `DeviceLockAndRemovePasscode` access right, [`LightsOutManagementLOM`](lightsoutmanagementlom.md) configuration and is available in macOS 11 and later on [`supported macOS devices`](https://developer.apple.comhttps://support.apple.com/guide/deployment/lights-out-management-payload-settings-dep580cf25bc/web).

`DeviceDNSName` is the `CommonName` in the Identity issued on the client certificate from [`LightsOutManagementLOM`](lightsoutmanagementlom.md). [`LOMSetupRequestResponse`](lomsetuprequestresponse.md) returns `PrimaryIPv6AddressList` and `SecondaryIPv6AddressList` after a successful deployment of Lights Out management configuration payload and subsequent [`LOMSetupRequestCommand`](lomsetuprequestcommand.md).

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
- [object LOMDeviceRequestCommand](lomdevicerequestcommand.md)
  The command to send requests to a device using lights-out management (LOM).
- [object LOMDeviceRequestResponse](lomdevicerequestresponse.md)
  A response from the device after it processes requests it receives through lights-out management (LOM).

## Request Body

The command to send requests to a device using lights-out management (LOM).

## See Also

- [LOM Setup Request Command](lom-setup-request-command.md)
  Get information from a device to set up lights-out management (LOM).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/lom-device-request-command)*