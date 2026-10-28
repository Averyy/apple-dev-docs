# requestConfirmation(result:confirmationActionName:showPrompt:)

**Framework**: App Intents  
**Kind**: method  
**Role**: Instance Method

Requests user confirmation before performing the app intent.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

> **Deprecated**: Please use requestConfirmation(conditions:actionName:dialog:) or requestConfirmation(conditions:actionName:dialog:showDialogAsPrompt:content:)

## Declaration

```swift
func requestConfirmation<Result>(result: Result, confirmationActionName: ConfirmationActionName = .`continue`, showPrompt: Bool = true) async throws where Result : IntentResult
```

## Discussion

Use [`requestConfirmation(conditions:actionName:dialog:)`](./requestconfirmation%28conditions,actionname,dialog%29.md) or [`requestConfirmation(conditions:actionName:dialog:showDialogAsPrompt:content:)`](./requestconfirmation%28conditions,actionname,dialog,showdialogasprompt,content%29.md) instead.

## See Also

### Deprecated
- [static var openAppWhenRun: Bool](./openappwhenrun.md)
  A Boolean property that tells the system to consider the app intent even if its app is not in the foreground.
- [func requestConfirmation<Result>(output: Result, confirmationActionName: ConfirmationActionName, showPrompt: Bool) async throws](./requestconfirmation%28output,confirmationactionname,showprompt%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/requestconfirmation(result:confirmationactionname:showprompt:))*