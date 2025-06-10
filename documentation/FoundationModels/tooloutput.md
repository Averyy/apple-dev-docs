# ToolOutput

**Framework**: Foundation Models  
**Kind**: struct

A structure that contains the output a tool generates.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct ToolOutput
```

## Mentions

- [Expanding generation with tool calling](expanding-generation-with-tool-calling.md)

## Topics

### Creating a tool output
- [init(_:)](tooloutput/init(_:).md)
  Creates a tool output with a generated encodable object.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func call(arguments: Self.Arguments) async throws -> ToolOutput](tool/call(arguments:).md)
  A language model will call this method when it wants to leverage this tool.
- [associatedtype Arguments : ConvertibleFromGeneratedContent](tool/arguments.md)
  The arguments that this tool should accept.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/tooloutput)*