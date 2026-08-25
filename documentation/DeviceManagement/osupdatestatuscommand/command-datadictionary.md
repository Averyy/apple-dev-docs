# OSUpdateStatusCommand.Command

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
object OSUpdateStatusCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `RequestType` (string) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/osupdatestatuscommand/command-data.dictionary)*