# LOMSetupRequestResponse.ErrorChainItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes an error chain item.

**Availability**:
- macOS 11.0+

## Declaration

```swift
object LOMSetupRequestResponse.ErrorChainItem
```

## Properties

- `ErrorCode` (integer) *(required)*: The error code.
- `ErrorDomain` (string) *(required)*: The error domain.
- `LocalizedDescription` (string) *(required)*: A description of the error in the device’s localized language.
- `USEnglishDescription` (string): A description of the error in U.S. English.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/lomsetuprequestresponse/errorchainitem)*