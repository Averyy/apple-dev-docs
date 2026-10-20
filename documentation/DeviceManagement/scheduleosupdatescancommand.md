# ScheduleOSUpdateScanCommand

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to schedule a background scan for operating-system updates on a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.

**Availability**:
- macOS 10.11+ - Deprecated in 26.0

> **Deprecated**: **Removed** Use the declarative management software update features instead.

## Declaration

```
object ScheduleOSUpdateScanCommand
```

## Topics

### Objects
- [object ScheduleOSUpdateScanCommand.Command](./scheduleosupdatescancommand/command-data.dictionary.md)
  The command to schedule a background scan for operating-system updates on a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.

## Properties

- `Command` (ScheduleOSUpdateScanCommand.Command) *(required)* *(deprecated)*: The command dictionary.
- `CommandUUID` (string) *(required)* *(deprecated)*: The unique identifier of the command.

## See Also

### Commands and responses
- [object ScheduleOSUpdateScanResponse](./scheduleosupdatescanresponse.md)
  A response from the device after it processes the command to schedule a background scan for operating-system updates on a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/scheduleosupdatescancommand)*