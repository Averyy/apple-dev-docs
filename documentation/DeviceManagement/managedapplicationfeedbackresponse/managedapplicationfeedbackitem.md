# ManagedApplicationFeedbackResponse.ManagedApplicationFeedbackItem

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

A dictionary that contains a managed app’s feedback item.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- macOS 11.0+
- tvOS 10.2+
- visionOS 1.1+

## Declaration

```
object ManagedApplicationFeedbackResponse.ManagedApplicationFeedbackItem
```

## Topics

### Objects
- [object ManagedApplicationFeedbackResponse.ManagedApplicationFeedbackItem.Feedback](./managedapplicationfeedbackitem/feedback-data.dictionary.md)
  A dictionary that contains a managed app’s feedback items.

## Properties

- `Feedback` (ManagedApplicationFeedbackResponse.ManagedApplicationFeedbackItem.Feedback): The app’s feedback.
- `Identifier` (string) *(required)*: The app’s bundle identifier.

## See Also

### Objects
- [object ManagedApplicationFeedbackResponse.ErrorChainItem](./errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managedapplicationfeedbackresponse/managedapplicationfeedbackitem)*