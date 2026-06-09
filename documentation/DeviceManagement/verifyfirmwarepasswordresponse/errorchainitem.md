# VerifyFirmwarePasswordResponse.ErrorChainItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes an error chain item.

**Availability**:
- macOS 10.13+

## Declaration

```swift
object VerifyFirmwarePasswordResponse.ErrorChainItem
```

## Properties

- `ErrorCode` (integer) *(required)*: The error code.
- `ErrorDomain` (string) *(required)*: The error domain.
- `LocalizedDescription` (string) *(required)*: A description of the error in the device’s localized language.
- `USEnglishDescription` (string): A description of the error in U.S. English.

## See Also

- [object VerifyFirmwarePasswordResponse.VerifyFirmwarePassword](verifyfirmwarepasswordresponse/verifyfirmwarepassword-data.dictionary.md)
  A dictionary containing the results of the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/verifyfirmwarepasswordresponse/errorchainitem)*