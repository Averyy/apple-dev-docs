# ScheduleOSUpdateScanCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to schedule a background scan for operating-system updates on a device.

**Availability**:
- macOS 10.11+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ScheduleOSUpdateScanCommand.Command
```

## Properties

- `Force` (boolean): If `true`, force a scan to start immediately. Otherwise, the scan starts at a system-determined time.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/scheduleosupdatescancommand/command-data.dictionary)*