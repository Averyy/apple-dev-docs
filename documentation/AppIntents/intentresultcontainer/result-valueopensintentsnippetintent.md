# result(value:opensIntent:snippetIntent:)

**Framework**: App Intents  
**Kind**: method

Indicates that a completed app intent displays an interactive snippet and returns a value and another intent to open the originating app.

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
static func result<Value>(value: Value, opensIntent: some AppIntent, snippetIntent: some SnippetIntent = EmptySnippetIntent()) -> Self where Self == IntentResultContainer<Value, Never, _SnippetIntentContainer, Never>, Value : _IntentValue
```

## Parameters

- `value`: The value that the app intent returns after completion.
- `opensIntent`: An app intent to open the originating app and show the   intent’s result.   additional functionality.
- `snippetIntent`: An app intent that displays an interactive snippet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresultcontainer/result(value:opensintent:snippetintent:))*