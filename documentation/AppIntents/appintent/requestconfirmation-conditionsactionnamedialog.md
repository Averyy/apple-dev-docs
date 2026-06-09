# requestConfirmation(conditions:actionName:dialog:)

**Framework**: App Intents  
**Kind**: method

Displays a confirmation prompt that includes the specified text and action details.

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

#### Discussion

Call this method when you want someone to confirm a particular choice. For example, call this method before someone performs an action that might be destructive or unsafe. The method displays a prompt that includes the provided information and asks the person to confirm or cancel the operation. The method returns normally if they confirm the operation, but throws an error if they cancel it.

## Parameters

- `conditions`: The conditions to check before asking for confirmation.
- `actionName`: The action associated with the request. The system puts the action name in the button that confirms the action.
- `dialog`: The localized text you want the confirmation request to display or speak.

## See Also

- [func requestConfirmation() async throws](appintent/requestconfirmation.md)
  Displays a prompt that asks the person for confirmation before performing the app intent.
- [func requestConfirmation<Content>(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog?, showDialogAsPrompt: Bool, content: () -> Content) async throws](appintent/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:content:).md)
  Displays a confirmation prompt with an interactive snippet.
- [func requestConfirmation<Snippet>(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog?, showDialogAsPrompt: Bool, snippetIntent: Snippet) async throws](appintent/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:snippetintent:)-3vewj.md)
  Displays a confirmation prompt that includes an interactive snippet.
- [func requestConfirmation<Snippet>(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog?, showDialogAsPrompt: Bool, snippetIntent: Snippet) async throws -> Snippet.PerformResult.Value](appintent/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:snippetintent:)-jxb8.md)
  Displays a confirmation prompt with an interactive snippet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/requestconfirmation(conditions:actionname:dialog:))*