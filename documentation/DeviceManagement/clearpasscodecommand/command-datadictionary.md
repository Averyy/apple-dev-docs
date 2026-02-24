# ClearPasscodeCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to remove the passcode from a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object ClearPasscodeCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.
- `UnlockToken` (data) *(required)*: The unlock token value that the device provides in its `TokenUpdateMessage` check-in message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/clearpasscodecommand/command-data.dictionary)*