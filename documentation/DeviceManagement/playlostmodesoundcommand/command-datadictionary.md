# PlayLostModeSoundCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to play the Lost Mode sound on a device that’s in Lost Mode.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 10.3+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object PlayLostModeSoundCommand.Command
```

## Properties

- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/playlostmodesoundcommand/command-data.dictionary)*