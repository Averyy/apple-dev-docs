# result(value:snippetIntent:)

**Framework**: App Intents  
**Kind**: method

Indicates that a completed app intent returns a value and displays an interactive snippet.

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
static func result<Value>(value: Value, snippetIntent: some SnippetIntent = EmptySnippetIntent()) -> Self where Self == IntentResultContainer<Value, Never, _SnippetIntentContainer, Never>, Value : _IntentValue
```

## Parameters

- `value`: The value that the app intent returns after completion.
- `snippetIntent`: An app intent that displays an interactive snippet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresult/result(value:snippetintent:))*