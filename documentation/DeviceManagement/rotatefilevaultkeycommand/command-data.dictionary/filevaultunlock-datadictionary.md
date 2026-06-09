# RotateFileVaultKeyCommand.Command.FileVaultUnlock

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains FileVault unlock options.

**Availability**:
- macOS 10.9+

## Declaration

```swift
object RotateFileVaultKeyCommand.Command.FileVaultUnlock
```

## Properties

- `Password` (string): A FileVault user’s password, or if using a CoreStorage volume, the personal recovery key.
- `PrivateKeyExport` (data): The data for a .p12 export of the private key for the current institutional recovery key, which requires that `KeyType` is `institutional`. The system ignores this key on APFS volumes. Deprecated: macOS 10.15+
- `PrivateKeyExportPassword` (string): The password for `PrivateKeyExport`. Either `Password` or both `PrivateKeyExport` and `PrivateKeyExportPassword` must be present. The system ignores this key on APFS volumes. Deprecated: macOS 10.15+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/rotatefilevaultkeycommand/command-data.dictionary/filevaultunlock-data.dictionary)*