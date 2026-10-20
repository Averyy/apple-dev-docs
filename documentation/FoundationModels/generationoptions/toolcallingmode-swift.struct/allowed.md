# allowed

**Framework**: Foundation Models  
**Kind**: property  
**Role**: Type Property

The model may or may not call tools.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static let allowed: GenerationOptions.ToolCallingMode
```

## Mentions

- [Expanding generation with tool calling](../../expanding-generation-with-tool-calling.md)

#### Discussion

This is the default.

## See Also

### Getting the tool calling modes
- [static let disallowed: GenerationOptions.ToolCallingMode](./disallowed.md)
  The model may not call any tool.
- [static let required: GenerationOptions.ToolCallingMode](./required.md)
  The model must call one or multiple tools.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/toolcallingmode-swift.struct/allowed)*