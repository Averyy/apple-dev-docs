# OSUpdateStatusCommand

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to get the status of operating-system updates on a device. Removed: subscribe to the declarative management `softwareupdate.install-state` status item.

**Availability**:
- iOS 9.0+ - Deprecated in 26.0
- iPadOS 9.0+ - Deprecated in 26.0
- Mac Catalyst 9.0+ - Deprecated in 26.0
- macOS 10.11.5+ - Deprecated in 26.0
- tvOS 12.0+ - Deprecated in 26.0

> **Deprecated**: **Removed** Use the declarative management software update features instead.

## Declaration

```
object OSUpdateStatusCommand
```

## Topics

### Objects
- [object OSUpdateStatusCommand.Command](./osupdatestatuscommand/command-data.dictionary.md)
  The command to get the status of operating-system updates on a device. Removed: subscribe to the declarative management `softwareupdate.install-state` status item.

## Properties

- `Command` (OSUpdateStatusCommand.Command) *(required)* *(deprecated)*: The command dictionary.
- `CommandUUID` (string) *(required)* *(deprecated)*: The unique identifier of the command.

## See Also

### Commands and responses
- [object OSUpdateStatusResponse](./osupdatestatusresponse.md)
  A response from the device after it processes the command to get the status of operating-system updates on a device. Removed: subscribe to the declarative management `softwareupdate.install-state` status item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/osupdatestatuscommand)*