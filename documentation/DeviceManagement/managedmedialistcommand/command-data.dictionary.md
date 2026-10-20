# ManagedMediaListCommand.Command

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to get a list of the managed books on a device.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+

## Declaration

```
object ManagedMediaListCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.

  **Default**: `false`
- `RequestType` (string) *(required)*: The request type for this command.

  **Allowed Values**: `ManagedMediaList`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managedmedialistcommand/command-data.dictionary)*