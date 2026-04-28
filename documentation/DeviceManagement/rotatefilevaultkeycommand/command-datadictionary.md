# RotateFileVaultKeyCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to change the FileVault primary password on a device.

**Availability**:
- macOS 10.9+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object RotateFileVaultKeyCommand.Command
```

## Topics

### Objects
- [object RotateFileVaultKeyCommand.Command.FileVaultUnlock](rotatefilevaultkeycommand/command-data.dictionary/filevaultunlock-data.dictionary.md)
  A dictionary that contains FileVault unlock options.

## Properties

- `FileVaultUnlock` (RotateFileVaultKeyCommand.Command.FileVaultUnlock) *(required)*: A dictionary that contains FileVault unlock options.
- `KeyType` (string) *(required)*: The type of FileVault key you want to change the password for. Set this value to `personal` and set a value for `Password` in the `FileVaultUnlock` dictionary to enable unlocking a device with a password. Set this value to `institutional` and set values for `PrivateKeyExport` and `PrivateKeyExportPassword` in the `FileVaultUnlock` dictionary.
- `NewCertificate` (data): A DER-encoded certificate for creating a new institutional recovery key, which the system requires if `KeyType` is `institutional`.
- `ReplyEncryptionCertificate` (data): A DER-encoded certificate for encrypting the new personal recovery key in a wrapper conforming to the IETF Cryptographic Message Syntax (CMS) standard.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/rotatefilevaultkeycommand/command-data.dictionary)*