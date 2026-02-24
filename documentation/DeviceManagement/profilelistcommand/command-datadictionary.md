# ProfileListCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to get a list of installed profiles on a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object ProfileListCommand.Command
```

## Properties

- `ManagedOnly` (boolean): If `true`, only include profiles that MDM has installed. For user enrollments, the device ignores this key and always limits the results to managed profiles. This value is available in iOS 13 and later, macOS 10.5 and later, and tvOS 13 and later.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/profilelistcommand/command-data.dictionary)*