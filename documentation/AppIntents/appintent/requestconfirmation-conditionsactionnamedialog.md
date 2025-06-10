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

## See Also

- [func requestConfirmation() async throws](appintent/requestconfirmation.md)
  Requests user confirmation before performing the app intent.
- [func requestConfirmation<Content>(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog?, showDialogAsPrompt: Bool, content: () -> Content) async throws](appintent/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:content:).md)
  Request user confirmation before performing the app intent.
- [func requestConfirmation<Result>(result: Result, confirmationActionName: ConfirmationActionName, showPrompt: Bool) async throws](appintent/requestconfirmation(result:confirmationactionname:showprompt:).md)
  Requests user confirmation before performing the app intent.
- [func requestConfirmation<Result>(output: Result, confirmationActionName: ConfirmationActionName, showPrompt: Bool) async throws](appintent/requestconfirmation(output:confirmationactionname:showprompt:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/requestconfirmation(conditions:actionname:dialog:))*