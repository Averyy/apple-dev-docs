# Arguments

**Framework**: Foundation Models  
**Kind**: associatedtype  
**Required**: Yes

The arguments that this tool should accept.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
associatedtype Arguments : ConvertibleFromGeneratedContent
```

## Mentions

- [Expanding generation with tool calling](expanding-generation-with-tool-calling.md)

#### Discussion

Typically arguments are either a [`Generable`](generable.md) type or `GeneratedContent.`

## See Also

- [func call(arguments: Self.Arguments) async throws -> ToolOutput](tool/call(arguments:).md)
  A language model will call this method when it wants to leverage this tool.
- [struct ToolOutput](tooloutput.md)
  A structure that contains the output a tool generates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/tool/arguments)*