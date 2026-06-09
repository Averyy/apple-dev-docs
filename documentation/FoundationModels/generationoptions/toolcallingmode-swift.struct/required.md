# required

**Framework**: Foundation Models  
**Kind**: property

The model must call one or multiple tools.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static let required: GenerationOptions.ToolCallingMode
```

## Mentions

- [Expanding generation with tool calling](expanding-generation-with-tool-calling.md)

#### Discussion

Please note that [`LanguageModelSession`](languagemodelsession.md) will loop until a `Tool` throws an error or this value is changed dynamically via `LanguageModelSession.Manifest`.

## See Also

- [static let allowed: GenerationOptions.ToolCallingMode](generationoptions/toolcallingmode-swift.struct/allowed.md)
  The model may or may not call tools.
- [static let disallowed: GenerationOptions.ToolCallingMode](generationoptions/toolcallingmode-swift.struct/disallowed.md)
  The model may not call any tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/toolcallingmode-swift.struct/required)*