# requestConfirmation(output:confirmationActionName:showPrompt:)

**Framework**: Swift  
**Kind**: method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
func requestConfirmation<Result>(output: Result, confirmationActionName: ConfirmationActionName = .`continue`, showPrompt: Bool = true) async throws where Result : IntentResult
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/never/requestconfirmation(output:confirmationactionname:showprompt:))*