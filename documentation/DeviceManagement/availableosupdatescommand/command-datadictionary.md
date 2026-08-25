# AvailableOSUpdatesCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to get a list of available operating-system updates for a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 12.0+

## Declaration

```swift
object AvailableOSUpdatesCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+
- `RequestType` (string) *(required)*: Removed: iOS 27+ | iPadOS 27+ | macOS 27+ | tvOS 27+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/availableosupdatescommand/command-data.dictionary)*