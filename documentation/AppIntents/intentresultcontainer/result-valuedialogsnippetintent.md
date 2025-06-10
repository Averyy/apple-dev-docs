# result(value:dialog:snippetIntent:)

**Framework**: App Intents  
**Kind**: method

Indicates that a completed app intent displays an interactive snippet with a dialog and returns a value.

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
static func result<Value>(value: Value, dialog: IntentDialog, snippetIntent: some SnippetIntent = EmptySnippetIntent()) -> Self where Self == IntentResultContainer<Value, Never, _SnippetIntentContainer, IntentDialog>, Value : _IntentValue
```

## Parameters

- `value`: The value produced by the 
- `dialog`: A custom success dialog
- `snippetIntent`: The intent responsible for presenting a snippet for this result


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresultcontainer/result(value:dialog:snippetintent:))*