# LanguageModelSession.ToolCallError

**Framework**: Foundation Models  
**Kind**: struct

An error that occurs while a system language model is calling a tool.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct ToolCallError
```

## Mentions

- [Expanding generation with tool calling](expanding-generation-with-tool-calling.md)

## Topics

### Creating a tool call error
- [init(tool: any Tool, underlyingError: any Error)](languagemodelsession/toolcallerror/init(tool:underlyingerror:).md)
  Creates a tool call error
### Getting the tool
- [var tool: any Tool](languagemodelsession/toolcallerror/tool.md)
  The tool that produced the error.
### Getting the error description
- [var errorDescription: String?](languagemodelsession/toolcallerror/errordescription.md)
  A string representation of the error description.
### Getting the underlying error
- [var underlyingError: any Error](languagemodelsession/toolcallerror/underlyingerror.md)
  The underlying error that was thrown during a tool call.
### Default Implementations
- [Error Implementations](languagemodelsession/toolcallerror/error-implementations.md)
- [LocalizedError Implementations](languagemodelsession/toolcallerror/localizederror-implementations.md)

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [LanguageModelSession.GenerationError](languagemodelsession/generationerror.md)
  An error that occurs while generating a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/toolcallerror)*