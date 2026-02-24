# InstalledApplicationListResponse.ErrorChainItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes an error chain item.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.7+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object InstalledApplicationListResponse.ErrorChainItem
```

## Properties

- `ErrorCode` (integer) *(required)*: The error code.
- `ErrorDomain` (string) *(required)*: The error domain.
- `LocalizedDescription` (string) *(required)*: A description of the error in the device’s localized language.
- `USEnglishDescription` (string): A description of the error in U.S. English.

## See Also

- [object InstalledApplicationListResponse.InstalledApplicationListItem](installedapplicationlistresponse/installedapplicationlistitem.md)
  A dictionary that describes an app list item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/installedapplicationlistresponse/errorchainitem)*