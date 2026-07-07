# requestConfirmation(output:confirmationActionName:showPrompt:)

**Framework**: App Intents  
**Kind**: method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func requestConfirmation<Result>(output: Result, confirmationActionName: ConfirmationActionName = .`continue`, showPrompt: Bool = true) async throws where Result : IntentResult
```

## See Also

- [static var openAppWhenRun: Bool](appintent/openappwhenrun.md)
  A Boolean property that tells the system to consider the app intent even if its app is not in the foreground.
- [func requestConfirmation<Result>(result: Result, confirmationActionName: ConfirmationActionName, showPrompt: Bool) async throws](appintent/requestconfirmation(result:confirmationactionname:showprompt:).md)
  Requests user confirmation before performing the app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/requestconfirmation(output:confirmationactionname:showprompt:))*