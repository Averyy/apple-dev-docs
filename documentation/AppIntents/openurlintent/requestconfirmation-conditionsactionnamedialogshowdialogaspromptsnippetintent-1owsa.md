# requestConfirmation(conditions:actionName:dialog:showDialogAsPrompt:snippetIntent:)

**Framework**: App Intents  
**Kind**: method

Requests user confirmation before performing the app intent.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
@discardableResult
func requestConfirmation<Snippet>(conditions: ConfirmationConditions = [], actionName: ConfirmationActionName = .`continue`, dialog: IntentDialog? = nil, showDialogAsPrompt: Bool = true, snippetIntent: Snippet) async throws -> Snippet.PerformResult.Value where Snippet : SnippetIntent, Snippet.PerformResult : ReturnsValue
```

#### Return Value

 The returned value of the Snippet Intent Perform Result

#### Discussion

The function displays an interactive snippet as a result of the app intent if a person confirms the action and otherwise throws an error.

> **Note**:  The app intent used to show the snippet confirmation can potentially execute side effects that modify the value passed in as a parameter to the caller. After returning from this function, ensure that the rest of the `perform` reads the most up-to-date information.

## Parameters

- `conditions`: The preconditions for requesting user confirmation.
- `actionName`: The name for the confirmation action.
- `dialog`: The confirmation dialog.
- `showDialogAsPrompt`: A flag that indicates whether the confirmation   dialog should appear as prompt text with the confirmation.
- `snippetIntent`: The intent responsible for presenting a snippet for this confirmation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/openurlintent/requestconfirmation(conditions:actionname:dialog:showdialogasprompt:snippetintent:)-1owsa)*