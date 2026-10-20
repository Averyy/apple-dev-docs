# ScheduleOSUpdateScanCommand.Command

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to schedule a background scan for operating-system updates on a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.

**Availability**:
- macOS 10.11+ - Deprecated in 26.0

> **Deprecated**: **Removed** Use the declarative management software update features instead.

## Declaration

```
object ScheduleOSUpdateScanCommand.Command
```

## Properties

- `Force` (boolean) *(deprecated)*: ~~If `true`, force a scan to start immediately. Otherwise, the scan starts at a system-determined time.~~

  ~~Deprecated: macOS 26+~~
  Removed: macOS 27+

  **Default**: `false`
- `RequestRequiresNetworkTether` (boolean) *(deprecated)*: ~~If `true`, the device needs to be network-tethered to run the command.~~

  ~~Deprecated: macOS 26+~~
  Removed: macOS 27+

  **Default**: `false`
- `RequestType` (string) *(required)* *(deprecated)*: ~~The request type for this command.~~

  ~~Deprecated: macOS 26+~~
  Removed: macOS 27+

  **Allowed Values**: `ScheduleOSUpdateScan`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/scheduleosupdatescancommand/command-data.dictionary)*