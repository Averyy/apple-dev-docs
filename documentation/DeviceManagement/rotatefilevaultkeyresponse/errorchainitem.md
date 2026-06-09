# RotateFileVaultKeyResponse.ErrorChainItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes an error chain item.

**Availability**:
- macOS 10.9+

## Declaration

```swift
object RotateFileVaultKeyResponse.ErrorChainItem
```

## Properties

- `ErrorCode` (integer) *(required)*: The error code.
- `ErrorDomain` (string) *(required)*: The error domain.
- `LocalizedDescription` (string) *(required)*: A description of the error in the device’s localized language.
- `USEnglishDescription` (string): A description of the error in U.S. English.

## See Also

- [object RotateFileVaultKeyResponse.RotateResult](rotatefilevaultkeyresponse/rotateresult-data.dictionary.md)
  The result of rotating the personal recovery key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/rotatefilevaultkeyresponse/errorchainitem)*