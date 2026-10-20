# requestConfirmation(output:confirmationActionName:showPrompt:)

**Framework**: App Intents  
**Kind**: method  
**Role**: Instance Method

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
func requestConfirmation<Result>(output: Result, confirmationActionName: ConfirmationActionName = .`continue`, showPrompt: Bool = true) async throws where Result : IntentResult
```

## See Also

### Deprecated
- [static var openAppWhenRun: Bool](./openappwhenrun.md)
  A Boolean property that tells the system to consider the app intent even if its app is not in the foreground.
- [func requestConfirmation<Result>(result: Result, confirmationActionName: ConfirmationActionName, showPrompt: Bool) async throws](./requestconfirmation%28result,confirmationactionname,showprompt%29.md)
  Requests user confirmation before performing the app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/requestconfirmation(output:confirmationactionname:showprompt:))*