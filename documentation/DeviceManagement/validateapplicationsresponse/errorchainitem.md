# ValidateApplicationsResponse.ErrorChainItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes an error chain item.

**Availability**:
- iOS 9.2+
- iPadOS 9.2+
- tvOS 10.2+
- visionOS 1.1+

## Declaration

```swift
object ValidateApplicationsResponse.ErrorChainItem
```

## Properties

- `ErrorCode` (integer) *(required)*: The error code.
- `ErrorDomain` (string) *(required)*: The error domain.
- `LocalizedDescription` (string) *(required)*: A description of the error in the device’s localized language.
- `USEnglishDescription` (string): A description of the error in U.S. English.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/validateapplicationsresponse/errorchainitem)*