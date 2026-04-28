# InviteToProgramCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to invite a user to join the Volume Purchase Program (VPP).

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- macOS 10.9+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object InviteToProgramCommand.Command
```

## Properties

- `InvitationURL` (string) *(required)*: The Volume Purchase Program (VPP) invitation URL.
- `ProgramID` (string) *(required)*: The program’s identifier, which can only be `com.apple.cloudvpp`.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/invitetoprogramcommand/command-data.dictionary)*