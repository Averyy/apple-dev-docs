# requestConfirmation()

**Framework**: App Intents  
**Kind**: method

Displays a prompt that asks the person for confirmation before performing the app intent.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func requestConfirmation() async throws
```

#### Discussion

Call this method before performing any work that might be destructive or unsafe. The method displays a prompt that asks the person to confirm or cancel the operation. The method returns normally if they confirm the operation, but throws an error if they cancel it.

## See Also

- [func requestConfirmation(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog) async throws](appintent/requestconfirmation(conditions:actionname:dialog:).md)
  Displays a confirmation prompt that includes the specified text and action details.
- [func requestConfirmation<Content>(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog?, showDialogAsPrompt: Bool, content: () -> Content) async throws](appintent/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:content:).md)
  Displays a confirmation prompt with an interactive snippet.
- [func requestConfirmation<Snippet>(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog?, showDialogAsPrompt: Bool, snippetIntent: Snippet) async throws](appintent/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:snippetintent:)-3vewj.md)
  Displays a confirmation prompt that includes an interactive snippet.
- [func requestConfirmation<Snippet>(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog?, showDialogAsPrompt: Bool, snippetIntent: Snippet) async throws -> Snippet.PerformResult.Value](appintent/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:snippetintent:)-jxb8.md)
  Displays a confirmation prompt with an interactive snippet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/requestconfirmation())*