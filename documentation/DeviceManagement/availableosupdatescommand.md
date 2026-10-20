# AvailableOSUpdatesCommand

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to get a list of available operating-system updates for a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.

**Availability**:
- iOS 9.0+ - Deprecated in 26.0
- iPadOS 9.0+ - Deprecated in 26.0
- Mac Catalyst 9.0+ - Deprecated in 26.0
- macOS 10.11+ - Deprecated in 26.0
- tvOS 12.0+ - Deprecated in 26.0

> **Deprecated**: **Removed** Use the declarative management software update features instead.

## Declaration

```
object AvailableOSUpdatesCommand
```

## Topics

### Objects
- [object AvailableOSUpdatesCommand.Command](./availableosupdatescommand/command-data.dictionary.md)
  The command to get a list of available operating-system updates for a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.

## Properties

- `Command` (AvailableOSUpdatesCommand.Command) *(required)* *(deprecated)*: The command dictionary.
- `CommandUUID` (string) *(required)* *(deprecated)*: The unique identifier of the command.

## See Also

### Commands and responses
- [object AvailableOSUpdatesResponse](./availableosupdatesresponse.md)
  A response from the device after it processes the command to get a list of available operating-system updates for a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/availableosupdatescommand)*