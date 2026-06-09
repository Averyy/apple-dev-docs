# prewarm(promptPrefix:)

**Framework**: Foundation Models  
**Kind**: method

Requests that the system eagerly load the resources required for this session into memory and optionally caches a prefix of your prompt.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
final func prewarm(promptPrefix: Prompt? = nil)
```

## Mentions

- [Optimizing key-value caching in language model sessions](optimizing-key-value-caching-in-language-model-sessions.md)

#### Discussion

This method can be useful in cases where you have a strong signal that the user will interact with session within a few seconds. For example, you might call prewarm when the user begins typing into a text field.

If you know a prefix for the future prompt, passing it to prewarm will allow the system to process the prompt eagerly and reduce latency for the future request.

> ❗ **Important**: You should only use prewarm when you have a window of at least 1 second before the call to a respond method, like [`respond(to:options:)`](languagemodelsession/respond(to:options:)-6a2gb.md) or [`streamResponse(to:options:)`](languagemodelsession/streamresponse(to:options:)-2nlni.md).

Calling this method does not guarantee that the system loads your assets immediately, particularly if your app is running in the background or the system is under load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/prewarm(promptprefix:))*