# Get the OS Update Status

**Framework**: Device Management  
**Kind**: httpRequest

Get the status of operating-system updates on a device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11.5+
- tvOS 12.0+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Query Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS, Shared iPad, tvOS |
| User Channel | - |
| Requires Supervision | iOS, macOS, tvOS |
| Allowed in User Enrollment | - |
| Required Access Right | AllowAppInstallation |

##### Example Request and Response

## Topics

### Command and Response
- [object OSUpdateStatusCommand](osupdatestatuscommand.md)
  The command to get the status of operating-system updates.
- [object OSUpdateStatusResponse](osupdatestatusresponse.md)
  A response from the device after it processes the command to get the status of operating-system updates.

## Request Body

The command to get the status of operating-system updates.

## See Also

- [Schedule an OS Update Scan](schedule-os-update-scan-command.md)
  Schedule a background scan for operating-system updates on a device.
- [List the Available OS Updates](available-os-updates-command.md)
  Get a list of available operating-system updates for a device.
- [Schedule an OS Update](schedule-os-update-command.md)
  Schedule an update of the operating system on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/os-update-status-command)*