# isResponding

**Framework**: Foundation Models  
**Kind**: property

A Boolean value that indicates a response is being generated.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final var isResponding: Bool { get }
```

## Mentions

- [Generating content and performing tasks with Foundation Models](generating-content-and-performing-tasks-with-foundation-models.md)

#### Discussion

> ❗ **Important**: Attempting to call any of the respond methods while this property is `true` is a programmer error.

## See Also

- [var transcript: Transcript](languagemodelsession/transcript.md)
  A full history of interactions, including user inputs and model responses.
- [var transcript: Transcript](languagemodelsession/transcript.md)
  A full history of interactions, including user inputs and model responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/isresponding)*