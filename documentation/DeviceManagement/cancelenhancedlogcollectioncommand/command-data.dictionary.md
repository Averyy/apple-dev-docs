# CancelEnhancedLogCollectionCommand.Command

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to cancel enhanced log collection on the device.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```
object CancelEnhancedLogCollectionCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.

  **Default**: `false`
- `RequestType` (string) *(required)*: The request type for this command.

  **Allowed Values**: `CancelEnhancedLogCollection`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/cancelenhancedlogcollectioncommand/command-data.dictionary)*