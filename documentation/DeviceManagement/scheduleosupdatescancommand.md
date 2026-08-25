# ScheduleOSUpdateScanCommand

**Framework**: Device Management  
**Kind**: dictionary

The command to schedule a background scan for operating-system updates on a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.

**Availability**:
- macOS 10.11+

## Declaration

```swift
object ScheduleOSUpdateScanCommand
```

## Topics

### Objects
- [object ScheduleOSUpdateScanCommand.Command](scheduleosupdatescancommand/command-data.dictionary.md)
  The command to schedule a background scan for operating-system updates on a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.

## Properties

- `Command` (ScheduleOSUpdateScanCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

- [object ScheduleOSUpdateScanResponse](scheduleosupdatescanresponse.md)
  A response from the device after it processes the command to schedule a background scan for operating-system updates on a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/scheduleosupdatescancommand)*