# ScheduleOSUpdateScanCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to schedule a background scan for operating-system updates on a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.

**Availability**:
- macOS 10.11+

## Declaration

```swift
object ScheduleOSUpdateScanCommand.Command
```

## Properties

- `Force` (boolean): Removed: macOS 27+
- `RequestRequiresNetworkTether` (boolean): Removed: macOS 27+
- `RequestType` (string) *(required)*: Removed: macOS 27+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/scheduleosupdatescancommand/command-data.dictionary)*