# DeviceConfiguredResponse.ErrorChainItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes an error chain item.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 10.2+
- visionOS 2.0+

## Declaration

```swift
object DeviceConfiguredResponse.ErrorChainItem
```

## Properties

- `ErrorCode` (integer) *(required)*: The error code.
- `ErrorDomain` (string) *(required)*: The error domain.
- `LocalizedDescription` (string) *(required)*: A description of the error in the device’s localized language.
- `USEnglishDescription` (string): A description of the error in U.S. English.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/deviceconfiguredresponse/errorchainitem)*