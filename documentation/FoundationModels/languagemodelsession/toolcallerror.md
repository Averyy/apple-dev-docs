# LanguageModelSession.ToolCallError

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

An error that occurs while a language model is calling a tool.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct ToolCallError
```

## Mentions

- [Expanding generation with tool calling](../expanding-generation-with-tool-calling.md)

## Topics

### Creating a tool call error
- [init(tool: any Tool, underlyingError: any Error)](./toolcallerror/init%28tool,underlyingerror%29.md)
  Creates a tool call error.
### Getting the tool
- [var tool: any Tool](./toolcallerror/tool.md)
  The tool that produced the error.
### Getting the error description
- [var errorDescription: String?](./toolcallerror/errordescription.md)
  A string representation of the error description.
### Getting the underlying error
- [var underlyingError: any Error](./toolcallerror/underlyingerror.md)
  The underlying error that was thrown during a tool call.
### Default Implementations
- [LocalizedError Implementations](./toolcallerror/localizederror-implementations.md)

## Relationships

### Conforms To
- [Error](../../Swift/error.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [LanguageModelSession.Error](./error.md)
  A failure caused by incorrect use of a language model session.
- [LanguageModelSession.GenerationError](./generationerror.md)
  An error that may occur while generating a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/toolcallerror)*