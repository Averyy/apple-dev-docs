# OS Update Status

**Framework**: Device Management  
**Kind**: httpRequest

Get the status of operating-system updates on a device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11.5+
- tvOS 12.0+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS |
| User channel | NA |
| Requires supervision | iOS, macOS, tvOS |
| Allowed in user enrollment | NA |
| Required access right | AllowAppInstallation |

##### Example Request and Response

## Topics

### Commands and responses
- [object OSUpdateStatusCommand](osupdatestatuscommand.md)
  The command to get the status of operating-system updates on a device.
- [object OSUpdateStatusResponse](osupdatestatusresponse.md)
  A response from the device after it processes the command to get the status of operating-system updates on a device.

## Request Body

The request object the server returns for the OS Update Status Command.

## See Also

- [Schedule OS Update Scan](schedule-os-update-scan-command.md)
  Schedule a background scan for operating-system updates on a device.
- [Available OS Updates](available-os-updates-command.md)
  Get a list of available operating-system updates for a device.
- [Schedule OS Update](schedule-os-update-command.md)
  Schedule an update of the operating system on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/os-update-status-command)*