# required

**Framework**: Foundation Models  
**Kind**: property  
**Role**: Type Property

The model must call one or multiple tools.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static let required: GenerationOptions.ToolCallingMode
```

## Mentions

- [Expanding generation with tool calling](../../expanding-generation-with-tool-calling.md)

## Discussion

[`LanguageModelSession`](../../languagemodelsession.md) keeps calling tools until a tool throws an error from its [`call(arguments:)`](../../tool/call%28arguments%29.md) method or you change the mode dynamically using a [`LanguageModelSession.DynamicProfile`](../../languagemodelsession/dynamicprofile.md).

## See Also

### Getting the tool calling modes
- [static let allowed: GenerationOptions.ToolCallingMode](./allowed.md)
  The model may or may not call tools.
- [static let disallowed: GenerationOptions.ToolCallingMode](./disallowed.md)
  The model may not call any tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/toolcallingmode-swift.struct/required)*