# ManagedApplicationListCommand

**Framework**: Device Management  
**Kind**: dictionary

The command to get the status of all managed apps on a device.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 5.0+
- macOS 11.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ManagedApplicationListCommand
```

## Topics

### Objects
- [object ManagedApplicationListCommand.Command](managedapplicationlistcommand/command-data.dictionary.md)
  The command to get the status of all managed apps on a device.

## Properties

- `Command` (ManagedApplicationListCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

- [object ManagedApplicationListResponse](managedapplicationlistresponse.md)
  A response from the device after it processes the command to get the status of all managed apps on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managedapplicationlistcommand)*