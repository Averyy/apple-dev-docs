# Available OS Updates

**Framework**: Device Management  
**Kind**: httpRequest

Get a list of available operating-system updates for a device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11+
- tvOS 12.0+

#### Discussion

This command is also available to execute on managed devices that aren’t enrolled in the Device Enrollment Program (DEP). A device must have a total of `DownloadSize` + `InstallSize` bytes available to successfully install a software update. In macOS, execute the `ScheduleOSUpdateScan` command to update the results that this command returns. In iOS and tvOS, the list only contains the latest available updates.

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
- [object AvailableOSUpdatesCommand](availableosupdatescommand.md)
  The command to get a list of available operating-system updates for a device.
- [object AvailableOSUpdatesResponse](availableosupdatesresponse.md)
  A response from the device after it processes the command to get a list of available operating-system updates for a device.

## Request Body

The request object the server returns for the Available OS Updates Command.

## See Also

- [Schedule OS Update Scan](schedule-os-update-scan-command.md)
  Schedule a background scan for operating-system updates on a device.
- [Schedule OS Update](schedule-os-update-command.md)
  Schedule an update of the operating system on a device.
- [OS Update Status](os-update-status-command.md)
  Get the status of operating-system updates on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/available-os-updates-command)*