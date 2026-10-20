# OSUpdateStatusCommand.Command

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
object OSUpdateStatusCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean) *(deprecated)*: ~~If `true`, the device needs to be network-tethered to run the command.~~

  ~~Deprecated: iOS 26+ | iPadOS 26+ | macOS 26+ | tvOS 26+~~
  Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+

  **Default**: `false`
- `RequestType` (string) *(required)* *(deprecated)*: ~~The request type for this command.~~

  ~~Deprecated: iOS 26+ | iPadOS 26+ | macOS 26+ | tvOS 26+~~
  Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+

  **Allowed Values**: `OSUpdateStatus`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/osupdatestatuscommand/command-data.dictionary)*