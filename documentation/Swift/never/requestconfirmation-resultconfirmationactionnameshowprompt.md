# requestConfirmation(result:confirmationActionName:showPrompt:)

**Framework**: Swift  
**Kind**: method

Requests user confirmation before performing the app intent.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+
- Unknown ?+ - Deprecated
- visionOS 1.0+

## Declaration

```swift
func requestConfirmation<Result>(result: Result, confirmationActionName: ConfirmationActionName = .`continue`, showPrompt: Bool = true) async throws where Result : IntentResult
```

#### Discussion

Use [`requestConfirmation(conditions:actionName:dialog:)`](never/requestconfirmation(conditions:actionname:dialog:).md) or `requestConfirmation(conditions:actionName:dialog:showDialogAsPrompt:content:)` instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/never/requestconfirmation(result:confirmationactionname:showprompt:))*