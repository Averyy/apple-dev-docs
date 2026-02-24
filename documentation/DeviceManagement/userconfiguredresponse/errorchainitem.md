# UserConfiguredResponse.ErrorChainItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes an error chain item.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
object UserConfiguredResponse.ErrorChainItem
```

## Properties

- `ErrorCode` (integer) *(required)*: The error code.
- `ErrorDomain` (string) *(required)*: The error domain.
- `LocalizedDescription` (string) *(required)*: A description of the error in the device’s localized language.
- `USEnglishDescription` (string): A description of the error in U.S. English.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/userconfiguredresponse/errorchainitem)*