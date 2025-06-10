# requestConfirmation(conditions:actionName:dialog:showDialogAsPrompt:content:)

**Framework**: App Intents  
**Kind**: method

Request user confirmation before performing the app intent.

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
func requestConfirmation<Content>(conditions: ConfirmationConditions = [], actionName: ConfirmationActionName = .`continue`, dialog: IntentDialog? = nil, showDialogAsPrompt: Bool = true, @ViewBuilder content: () -> Content) async throws where Content : View
```

## Parameters

- `conditions`: The preconditions for requesting confirmation.
- `actionName`: The name for the confirmation action.
- `dialog`: The confirmation dialog.
- `showDialogAsPrompt`: Flag indicating whether the confirmation   dialog should be displayed as prompt text with the confirmation.
- `content`: The   to display for confirmation.

## See Also

- [func requestConfirmation() async throws](appintent/requestconfirmation.md)
  Requests user confirmation before performing the app intent.
- [func requestConfirmation(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog) async throws](appintent/requestconfirmation(conditions:actionname:dialog:).md)
  Requests user confirmation before performing the app intent.
- [func requestConfirmation<Result>(result: Result, confirmationActionName: ConfirmationActionName, showPrompt: Bool) async throws](appintent/requestconfirmation(result:confirmationactionname:showprompt:).md)
  Requests user confirmation before performing the app intent.
- [func requestConfirmation<Result>(output: Result, confirmationActionName: ConfirmationActionName, showPrompt: Bool) async throws](appintent/requestconfirmation(output:confirmationactionname:showprompt:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:content:))*