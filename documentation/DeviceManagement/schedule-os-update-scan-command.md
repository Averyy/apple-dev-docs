# Schedule an OS Update Scan

**Framework**: Device Management  
**Kind**: httpRequest

Schedule a background scan for operating-system updates on a device.

**Availability**:
- macOS 10.11+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | macOS |
| User Channel | - |
| Requires Supervision | macOS |
| Allowed in User Enrollment | - |
| Required Access Right | - |

##### Example Request and Response

## Topics

### Command and Response
- [object ScheduleOSUpdateScanCommand](scheduleosupdatescancommand.md)
  The command to schedule an operating-system update scan.
- [object ScheduleOSUpdateScanResponse](scheduleosupdatescanresponse.md)
  A response from the device after it processes the command to schedule an operating-system update scan.

## Request Body

The command to schedule an operating-system update scan.

## See Also

- [List the Available OS Updates](available-os-updates-command.md)
  Get a list of available operating-system updates for a device.
- [Schedule an OS Update](schedule-os-update-command.md)
  Schedule an update of the operating system on a device.
- [Get the OS Update Status](os-update-status-command.md)
  Get the status of operating-system updates on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/schedule-os-update-scan-command)*