# call(arguments:)

**Framework**: Foundation Models  
**Kind**: method  
**Required**: Yes

A language model will call this method when it wants to leverage this tool.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func call(arguments: Self.Arguments) async throws -> ToolOutput
```

## Mentions

- [Expanding generation with tool calling](expanding-generation-with-tool-calling.md)

#### Discussion

If errors are throw in the body of this method, they will be wrapped in a `LanguageModelSession.ToolCallError` and rethrown at the call site of `LanguageModelSession.respond(to:)`.

> **Note**: This method may be invoked concurrently with itself or with other tools.

## See Also

- [struct ToolOutput](tooloutput.md)
  A structure that contains the output a tool generates.
- [associatedtype Arguments : ConvertibleFromGeneratedContent](tool/arguments.md)
  The arguments that this tool should accept.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/tool/call(arguments:))*