# ClearActivationLockBypassCodeResponse.ErrorChainItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes an error chain item.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 7.1+
- macOS 10.15+
- visionOS 2.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ClearActivationLockBypassCodeResponse.ErrorChainItem
```

## Properties

- `ErrorCode` (integer) *(required)*: The error code.
- `ErrorDomain` (string) *(required)*: The error domain.
- `LocalizedDescription` (string) *(required)*: A description of the error in the device’s localized language.
- `USEnglishDescription` (string): A description of the error in U.S. English.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/clearactivationlockbypasscoderesponse/errorchainitem)*