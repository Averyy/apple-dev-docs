# ManagedApplicationFeedbackResponse.ErrorChainItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes an error chain item.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- macOS 11.0+
- tvOS 10.2+
- visionOS 1.1+

## Declaration

```swift
object ManagedApplicationFeedbackResponse.ErrorChainItem
```

## Properties

- `ErrorCode` (integer) *(required)*: The error code.
- `ErrorDomain` (string) *(required)*: The error domain.
- `LocalizedDescription` (string) *(required)*: A description of the error in the device’s localized language.
- `USEnglishDescription` (string): A description of the error in U.S. English.

## See Also

- [object ManagedApplicationFeedbackResponse.ManagedApplicationFeedbackItem](managedapplicationfeedbackresponse/managedapplicationfeedbackitem.md)
  A dictionary that contains a managed app’s feedback item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managedapplicationfeedbackresponse/errorchainitem)*