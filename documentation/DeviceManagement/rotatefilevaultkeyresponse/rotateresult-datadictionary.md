# RotateFileVaultKeyResponse.RotateResult

**Framework**: Device Management  
**Kind**: dictionary

The result of rotating the personal recovery key.

**Availability**:
- macOS 10.9+

## Declaration

```swift
object RotateFileVaultKeyResponse.RotateResult
```

## Properties

- `EncryptedNewRecoveryKey` (data): A new personal recovery key that’s encrypted using a `ReplyEncryptionCertificate` as a CMS-compliant envelope.

## See Also

- [object RotateFileVaultKeyResponse.ErrorChainItem](rotatefilevaultkeyresponse/errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/rotatefilevaultkeyresponse/rotateresult-data.dictionary)*