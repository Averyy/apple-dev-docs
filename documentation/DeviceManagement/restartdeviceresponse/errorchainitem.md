# RestartDeviceResponse.ErrorChainItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes an error chain item.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 10.3+
- macOS 10.13+
- tvOS 10.2+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object RestartDeviceResponse.ErrorChainItem
```

## Properties

- `ErrorCode` (integer) *(required)*: The error code.
- `ErrorDomain` (string) *(required)*: The error domain.
- `LocalizedDescription` (string) *(required)*: A description of the error in the device’s localized language.
- `USEnglishDescription` (string): A description of the error in U.S. English.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/restartdeviceresponse/errorchainitem)*