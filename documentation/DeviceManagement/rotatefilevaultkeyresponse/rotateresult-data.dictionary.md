# RotateFileVaultKeyResponse.RotateResult

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The result of rotating the personal recovery key.

**Availability**:
- macOS 10.9+

## Declaration

```
object RotateFileVaultKeyResponse.RotateResult
```

## Properties

- `EncryptedNewRecoveryKey` (data): A new personal recovery key that’s encrypted using a `ReplyEncryptionCertificate` as a CMS-compliant envelope.

## See Also

### Objects
- [object RotateFileVaultKeyResponse.ErrorChainItem](./errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/rotatefilevaultkeyresponse/rotateresult-data.dictionary)*