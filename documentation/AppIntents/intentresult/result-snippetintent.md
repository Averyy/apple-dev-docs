# result(snippetIntent:)

**Framework**: App Intents  
**Kind**: method

Indicates that a completed app intent displays an interactive snippet.

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
static func result(snippetIntent: some SnippetIntent = EmptySnippetIntent()) -> Self where Self == IntentResultContainer<Never, Never, _SnippetIntentContainer, Never>
```

## Parameters

- `snippetIntent`: An app intent that displays an interactive snippet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresult/result(snippetintent:))*