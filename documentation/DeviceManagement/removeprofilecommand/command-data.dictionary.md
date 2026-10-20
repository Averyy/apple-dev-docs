# RemoveProfileCommand.Command

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to remove a previously installed profile from the device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```
object RemoveProfileCommand.Command
```

## Properties

- `Identifier` (string) *(required)*: The identifier of the profile to remove.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.

  **Default**: `false`
- `RequestType` (string) *(required)*: The request type for this command.

  **Allowed Values**: `RemoveProfile`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/removeprofilecommand/command-data.dictionary)*