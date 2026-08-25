# OSUpdateStatusCommand

**Framework**: Device Management  
**Kind**: dictionary

The command to get the status of operating-system updates on a device. Removed: subscribe to the declarative management `softwareupdate.install-state` status item.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11.5+
- tvOS 12.0+

## Declaration

```swift
object OSUpdateStatusCommand
```

## Topics

### Objects
- [object OSUpdateStatusCommand.Command](osupdatestatuscommand/command-data.dictionary.md)
  The command to get the status of operating-system updates on a device. Removed: subscribe to the declarative management `softwareupdate.install-state` status item.

## Properties

- `Command` (OSUpdateStatusCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

- [object OSUpdateStatusResponse](osupdatestatusresponse.md)
  A response from the device after it processes the command to get the status of operating-system updates on a device. Removed: subscribe to the declarative management `softwareupdate.install-state` status item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/osupdatestatuscommand)*