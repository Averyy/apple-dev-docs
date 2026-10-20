# ScheduleOSUpdateCommand

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to schedule an update of the operating system on a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.

**Availability**:
- iOS 9.0+ - Deprecated in 26.0
- iPadOS 9.0+ - Deprecated in 26.0
- Mac Catalyst 9.0+ - Deprecated in 26.0
- macOS 10.11+ - Deprecated in 26.0
- tvOS 12.0+ - Deprecated in 26.0

> **Deprecated**: **Removed** Use the declarative management software update features instead.

## Declaration

```
object ScheduleOSUpdateCommand
```

## Topics

### Objects
- [object ScheduleOSUpdateCommand.Command](./scheduleosupdatecommand/command-data.dictionary.md)
  The command to schedule an update of the operating system on a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.

## Properties

- `Command` (ScheduleOSUpdateCommand.Command) *(required)* *(deprecated)*: The command dictionary.
- `CommandUUID` (string) *(required)* *(deprecated)*: The unique identifier of the command.

## See Also

### Commands and responses
- [object ScheduleOSUpdateResponse](./scheduleosupdateresponse.md)
  A response from the device after it processes the command to schedule an update of the operating system on a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/scheduleosupdatecommand)*