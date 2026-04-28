# ScheduleOSUpdateCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to schedule an update of the operating system on a device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 12.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ScheduleOSUpdateCommand.Command
```

## Topics

### Objects
- [object ScheduleOSUpdateCommand.Command.UpdatesItem](scheduleosupdatecommand/command-data.dictionary/updatesitem.md)
  A dictionary that describes the available operating-system updates item.

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.
- `Updates` ([ScheduleOSUpdateCommand.Command.UpdatesItem]) *(required)*: An array of dictionaries specifying the updates to download or install. If this value is missing, the device applies the default behavior for handling updates. The device ignores this command and an informational error is returned, if a software update is managed by a Declarative Device Management [`SoftwareUpdateEnforcementSpecific`](softwareupdateenforcementspecific.md) configuration, as the configuration takes precedence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/scheduleosupdatecommand/command-data.dictionary)*