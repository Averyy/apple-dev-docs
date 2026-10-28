# LanguageModelError.contextSizeExceeded(_:)

**Framework**: Foundation Models  
**Kind**: case  
**Role**: Case

The session’s transcript exceeded the model’s context size.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
case contextSizeExceeded(LanguageModelError.ContextSizeExceeded)
```

## Mentions

- [Managing the context window](../managing-the-context-window.md)
- [Analyzing the runtime performance of your Foundation Models app](../analyzing-the-runtime-performance-of-your-foundation-models-app.md)
- [Generating content and performing tasks with Foundation Models](../generating-content-and-performing-tasks-with-foundation-models.md)
- [Inspecting session transcripts and reporting model feedback](../inspecting-session-transcripts-and-reporting-model-feedback.md)
- [Optimizing key-value caching in language model sessions](../optimizing-key-value-caching-in-language-model-sessions.md)

## Discussion

You can recover from this error by removing entries from the transcript and trying again.

For more information on managing the context window size, see [Managing the context window](../managing-the-context-window.md).

## See Also

### Exceeded context size error
- [LanguageModelError.ContextSizeExceeded](./contextsizeexceeded.md)
  Information about exceeding the context window size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/contextsizeexceeded(_:))*