# requestConfirmation()

**Framework**: App Intents  
**Kind**: method  
**Role**: Instance Method

Displays a prompt that asks the person for confirmation before performing the app intent.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
func requestConfirmation() async throws
```

## Discussion

Call this method before performing any work that might be destructive or unsafe. The method displays a prompt that asks the person to confirm or cancel the operation. The method returns normally if they confirm the operation, but throws an error if they cancel it.

## See Also

### Requesting confirmation
- [func requestConfirmation(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog) async throws](./requestconfirmation%28conditions,actionname,dialog%29.md)
  Displays a confirmation prompt that includes the specified text and action details.
- [func requestConfirmation<Content>(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog?, showDialogAsPrompt: Bool, content: () -> Content) async throws](./requestconfirmation%28conditions,actionname,dialog,showdialogasprompt,content%29.md)
  Displays a confirmation prompt with an interactive snippet.
- [func requestConfirmation<Snippet>(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog?, showDialogAsPrompt: Bool, snippetIntent: Snippet) async throws](./requestconfirmation%28conditions,actionname,dialog,showdialogasprompt,snippetintent%29-3vewj.md)
  Displays a confirmation prompt that includes an interactive snippet.
- [func requestConfirmation<Snippet>(conditions: ConfirmationConditions, actionName: ConfirmationActionName, dialog: IntentDialog?, showDialogAsPrompt: Bool, snippetIntent: Snippet) async throws -> Snippet.PerformResult.Value](./requestconfirmation%28conditions,actionname,dialog,showdialogasprompt,snippetintent%29-jxb8.md)
  Displays a confirmation prompt with an interactive snippet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/requestconfirmation())*