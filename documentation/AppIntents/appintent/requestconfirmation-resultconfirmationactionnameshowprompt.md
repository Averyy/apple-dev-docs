# requestConfirmation(result:confirmationActionName:showPrompt:)

**Framework**: App Intents  
**Kind**: method

Requests user confirmation before performing the app intent.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- visionOS ?+
- watchOS 9.0+
- Unknown ?+ - Deprecated
- tvOS 16.0+

## Declaration

```swift
func requestConfirmation<Result>(result: Result, confirmationActionName: ConfirmationActionName = .`continue`, showPrompt: Bool = true) async throws where Result : IntentResult
```

#### Discussion

Use [`requestConfirmation(conditions:actionName:dialog:)`](appintent/requestconfirmation(conditions:actionname:dialog:).md) or [`requestConfirmation(conditions:actionName:dialog:showDialogAsPrompt:content:)`](appintent/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:content:).md) instead.

## See Also

- [func requestConfirmation() async throws](appintent/requestconfirmation.md)
  Requests user confirmation before performing the app intent.
- [func requestConfirmation(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog) async throws](appintent/requestconfirmation(conditions:actionname:dialog:).md)
  Requests user confirmation before performing the app intent.
- [func requestConfirmation<Content>(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog?, showDialogAsPrompt: Bool, content: () -> Content) async throws](appintent/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:content:).md)
  Request user confirmation before performing the app intent.
- [func requestConfirmation<Result>(output: Result, confirmationActionName: ConfirmationActionName, showPrompt: Bool) async throws](appintent/requestconfirmation(output:confirmationactionname:showprompt:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/requestconfirmation(result:confirmationactionname:showprompt:))*