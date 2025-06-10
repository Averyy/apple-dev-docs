# requestConfirmation(conditions:actionName:dialog:showDialogAsPrompt:snippetIntent:)

**Framework**: Swift  
**Kind**: method

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func requestConfirmation<Snippet>(conditions: ConfirmationConditions = [], actionName: ConfirmationActionName = .`continue`, dialog: IntentDialog? = nil, showDialogAsPrompt: Bool = true, snippetIntent: Snippet) async throws where Snippet : SnippetIntent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/never/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:snippetintent:)-888lr)*