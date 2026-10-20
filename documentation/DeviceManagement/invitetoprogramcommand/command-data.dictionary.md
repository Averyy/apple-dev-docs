# InviteToProgramCommand.Command

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The command to invite a user to join the Volume Purchase Program (VPP).

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- macOS 10.9+

## Declaration

```
object InviteToProgramCommand.Command
```

## Properties

- `InvitationURL` (string) *(required)*: The Volume Purchase Program (VPP) invitation URL.
- `ProgramID` (string) *(required)*: The program’s identifier, which can only be `com.apple.cloudvpp`.

  **Allowed Values**: `com.apple.cloudvpp`
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.

  **Default**: `false`
- `RequestType` (string) *(required)*: The request type for this command.

  **Allowed Values**: `InviteToProgram`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/invitetoprogramcommand/command-data.dictionary)*