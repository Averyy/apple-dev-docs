# result(opensIntent:snippetIntent:)

**Framework**: App Intents  
**Kind**: method

Indicates that a completed app intent displays an interactive snippet and returns another intent to open the originating app.

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
static func result(opensIntent: some AppIntent, snippetIntent: some SnippetIntent = EmptySnippetIntent()) -> Self where Self == IntentResultContainer<Never, Never, _SnippetIntentContainer, Never>
```

## Parameters

- `opensIntent`: An app intent to open the originating app and show the   intent’s result.
- `snippetIntent`: The intent responsible for presenting a snippet for this result


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresultcontainer/result(opensintent:snippetintent:))*