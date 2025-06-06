# RotateFileVaultKeyResponse

**Framework**: Device Management  
**Kind**: dictionary

A response from the device after it processes the command to change the FileVault primary password.

**Availability**:
- macOS 10.9+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object RotateFileVaultKeyResponse
```

## Topics

### Commands
- [object RotateFileVaultKeyResponse.RotateResult](rotatefilevaultkeyresponse/rotateresult-data.dictionary.md)
  The result of rotating the personal recovery key.
- [object RotateFileVaultKeyResponse.ErrorChainItem](rotatefilevaultkeyresponse/errorchainitem.md)
  A dictionary that describes an error chain item.

## See Also

- [object RotateFileVaultKeyCommand](rotatefilevaultkeycommand.md)
  The command to change the FileVault primary password.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/rotatefilevaultkeyresponse)*