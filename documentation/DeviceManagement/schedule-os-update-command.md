# Schedule OS Update

**Framework**: Device Management  
**Kind**: httpRequest

Schedule an update of the operating system on a device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11+
- tvOS 12.0+

#### Discussion

Only supervised iOS, macOS, and tvOS devices are eligible for software update management.

This command can only schedule operating-system updates in iOS and tvOS, however, it can also schedule a variety of system software updates in macOS.

Downloading and installing updates in iOS and tvOS is a two-step process. Send a `ScheduleOSUpdate` command with `Default` for `InstallAction` to download the updates. Then send another `ScheduleOSUpdate` command with a `Default` `InstallAction` to install the updates. Software updates may require a restart, which prevents the device from responding. When this happens, the MDM server resends the `ScheduleOSUpdate` command when the device checks in again, however, the device won’t return a value for `UpdateResults`.

This command uses the [`ScheduleOSUpdateCommand.Command.UpdatesItem`](scheduleosupdatecommand/command-data.dictionary/updatesitem.md) `InstallAction` values to offer varying degrees of control to the user of a device. The user can control the update with the `NotifyOnly` and `DownloadOnly` actions, which don’t initiate the update process at all. The `InstallASAP` and `InstallForceRestart` actions attempt to install the update as soon as possible. On iOS devices with a passcode, the user must authorize the update by entering their passcode, allowing them to defer the update a limited number of times. After the user reaches that limit, the system prompts to update every time the device returns to the home screen. This makes the device virtually unusable until the user approves the software update. On macOS devices, the `InstallLater` action provides a similar behavior, which specifies how many times the user may defer the update before it’s forced.

A device may return a different `InstallAction` than requested.

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
- [object ScheduleOSUpdateCommand](scheduleosupdatecommand.md)
  The command to schedule an update of the operating system on a device.
- [object ScheduleOSUpdateResponse](scheduleosupdateresponse.md)
  A response from the device after it processes the command to schedule an update of the operating system on a device.

## Request Body

The request object the server returns for the Schedule OS Update Command.

## See Also

- [Schedule OS Update Scan](schedule-os-update-scan-command.md)
  Schedule a background scan for operating-system updates on a device.
- [Available OS Updates](available-os-updates-command.md)
  Get a list of available operating-system updates for a device.
- [OS Update Status](os-update-status-command.md)
  Get the status of operating-system updates on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/schedule-os-update-command)*