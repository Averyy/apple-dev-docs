# ApplyRedemptionCodeCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to complete the installation of an app using a redemption code.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 5.0+

## Declaration

```swift
object ApplyRedemptionCodeCommand.Command
```

## Properties

- `Identifier` (string) *(required)*: The bundle identifier of the app.
- `RedemptionCode` (string) *(required)*: The redemption code that applies to the app pending installation.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/applyredemptioncodecommand/command-data.dictionary)*