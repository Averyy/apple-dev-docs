# List the Available OS Updates

**Framework**: Device Management  
**Kind**: httpRequest

Get a list of available operating-system updates for a device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11+
- tvOS 12.0+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This command is also available to execute on managed devices that aren’t enrolled in the Device Enrollment Program (DEP). A device must have a total of `DownloadSize` + `InstallSize` bytes available to successfully install a software update. In macOS, execute the `ScheduleOSUpdateScan` command to update the results that this command returns. In iOS and tvOS, the list only contains the latest available updates.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Query Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS, Shared iPad, tvOS |
| User Channel | - |
| Requires Supervision | iOS, tvOS |
| Allowed in User Enrollment | - |
| Required Access Right | AllowAppInstallation |

##### Example Request and Response

## Topics

### Command and Response
- [object AvailableOSUpdatesCommand](availableosupdatescommand.md)
  The command to get a list of available operating-system updates.
- [object AvailableOSUpdatesResponse](availableosupdatesresponse.md)
  A response from the device after it processes the command to get a list of available operating-system updates.

## Request Body

The command to get a list of available operating-system updates.

## See Also

- [Schedule an OS Update Scan](schedule-os-update-scan-command.md)
  Schedule a background scan for operating-system updates on a device.
- [Schedule an OS Update](schedule-os-update-command.md)
  Schedule an update of the operating system on a device.
- [Get the OS Update Status](os-update-status-command.md)
  Get the status of operating-system updates on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/available-os-updates-command)*