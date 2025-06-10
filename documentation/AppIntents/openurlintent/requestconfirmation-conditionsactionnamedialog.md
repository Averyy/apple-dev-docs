# requestConfirmation(conditions:actionName:dialog:)

**Framework**: App Intents  
**Kind**: method

Requests user confirmation before performing the app intent.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func requestConfirmation(conditions: ConfirmationConditions = [], actionName: ConfirmationActionName = .`continue`, dialog: IntentDialog) async throws
```

## Parameters

- `conditions`: The preconditions for requesting confirmation.
- `actionName`: The name for the confirmation action.
- `dialog`: The confirmation dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/openurlintent/requestconfirmation(conditions:actionname:dialog:))*