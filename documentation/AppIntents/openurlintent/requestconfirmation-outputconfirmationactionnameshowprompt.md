# requestConfirmation(output:confirmationActionName:showPrompt:)

**Framework**: App Intents  
**Kind**: method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+
- Unknown ?+ - Deprecated
- Mac Catalyst ?+

## Declaration

```swift
func requestConfirmation<Result>(output: Result, confirmationActionName: ConfirmationActionName = .`continue`, showPrompt: Bool = true) async throws where Result : IntentResult
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/openurlintent/requestconfirmation(output:confirmationactionname:showprompt:))*