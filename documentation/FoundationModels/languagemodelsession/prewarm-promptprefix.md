# prewarm(promptPrefix:)

**Framework**: Foundation Models  
**Kind**: method

Loads the resources required for this session into memory, and optionally caches a prefix of your prompt to reduce request latency.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func prewarm(promptPrefix: Prompt? = nil)
```

## Mentions

- [Analyzing the runtime performance of your Foundation Models app](analyzing-the-runtime-performance-of-your-foundation-models-app.md)

#### Discussion

Use this method when you know a person will launch and interact with your session within a few seconds to preload the required session resources. For example, you might call this method when a person begins typing into a text field.

If you have a prefix for a future prompt, passing it to this method allows the system to process the prompt eagerly and reduce latency for the future request.

> ❗ **Important**: Only use this method when you have at least one second before calling a respond method, like [`respond(to:options:)`](languagemodelsession/respond(to:options:).md) or [`streamResponse(to:options:)`](languagemodelsession/streamresponse(to:options:).md).

Calling this method doesn’t guarantee that the system loads your resources immediately, particularly if your app is running in the background or the system is under load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/prewarm(promptprefix:))*