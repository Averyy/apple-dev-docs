# SettingsResponse.ErrorChainItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes an error chain item.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object SettingsResponse.ErrorChainItem
```

## Properties

- `ErrorCode` (integer) *(required)*: The error code.
- `ErrorDomain` (string) *(required)*: The error domain.
- `LocalizedDescription` (string) *(required)*: A description of the error in the device’s localized language.
- `USEnglishDescription` (string): A description of the error in U.S. English.

## See Also

- [object SettingsResponse.Settings](settingsresponse/settings-data.dictionary.md)
  A dictionary that describes the results of configuring settings on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/settingsresponse/errorchainitem)*