# SetFirmwarePasswordResponse.ErrorChainItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes an error chain item.

**Availability**:
- macOS 10.13+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SetFirmwarePasswordResponse.ErrorChainItem
```

## Properties

- `ErrorCode` (integer) *(required)*: The error code.
- `ErrorDomain` (string) *(required)*: The error domain.
- `LocalizedDescription` (string) *(required)*: A description of the error in the device’s localized language.
- `USEnglishDescription` (string): A description of the error in U.S. English.

## See Also

- [object SetFirmwarePasswordResponse.SetFirmwarePassword](setfirmwarepasswordresponse/setfirmwarepassword-data.dictionary.md)
  A dictionary that describes the result of a command to change the firmware password.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/setfirmwarepasswordresponse/errorchainitem)*