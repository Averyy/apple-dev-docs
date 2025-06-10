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

Use [`requestConfirmation(conditions:actionName:dialog:)`](openurlintent/requestconfirmation(conditions:actionname:dialog:).md) or `requestConfirmation(conditions:actionName:dialog:showDialogAsPrompt:content:)` instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/openurlintent/requestconfirmation(result:confirmationactionname:showprompt:))*