# requestConfirmation(conditions:actionName:dialog:showDialogAsPrompt:snippetIntent:)

**Framework**: App Intents  
**Kind**: method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func requestConfirmation<Snippet>(conditions: ConfirmationConditions = [], actionName: ConfirmationActionName = .`continue`, dialog: IntentDialog? = nil, showDialogAsPrompt: Bool = true, snippetIntent: Snippet) async throws where Snippet : SnippetIntent
```

## Mentions

- [Displaying static and interactive snippets](displaying-static-and-interactive-snippets.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:snippetintent:)-3vewj)*