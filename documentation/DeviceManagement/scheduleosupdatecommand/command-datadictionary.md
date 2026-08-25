# ScheduleOSUpdateCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to schedule an update of the operating system on a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 12.0+

## Declaration

```swift
object ScheduleOSUpdateCommand.Command
```

## Topics

### Objects
- [object ScheduleOSUpdateCommand.Command.UpdatesItem](scheduleosupdatecommand/command-data.dictionary/updatesitem.md)
  A dictionary that describes the available operating-system updates item.

## Properties

- `RequestRequiresNetworkTether` (boolean): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `RequestType` (string) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `Updates` ([ScheduleOSUpdateCommand.Command.UpdatesItem]) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/scheduleosupdatecommand/command-data.dictionary)*