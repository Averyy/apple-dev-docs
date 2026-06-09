# RotateFileVaultKeyCommand

**Framework**: Device Management  
**Kind**: dictionary

The command to change the FileVault primary password on a device.

**Availability**:
- macOS 10.9+

## Declaration

```swift
object RotateFileVaultKeyCommand
```

## Topics

### Objects
- [object RotateFileVaultKeyCommand.Command](rotatefilevaultkeycommand/command-data.dictionary.md)
  The command to change the FileVault primary password on a device.

## Properties

- `Command` (RotateFileVaultKeyCommand.Command) *(required)*: The command dictionary.
- `CommandUUID` (string) *(required)*: The unique identifier of the command.

## See Also

- [object RotateFileVaultKeyResponse](rotatefilevaultkeyresponse.md)
  A response from the device after it processes the command to change the FileVault primary password on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/rotatefilevaultkeycommand)*