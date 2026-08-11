# GenerationOptions.ToolCallingMode

**Framework**: Foundation Models  
**Kind**: struct

A value you use to describe the model behavior when it comes to tool usage.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct ToolCallingMode
```

## Mentions

- [Expanding generation with tool calling](expanding-generation-with-tool-calling.md)

#### Overview

Use this to control how the model interacts with tools for a given request. Tool calling mode supports three modes:

- **[`allowed`](generationoptions/toolcallingmode-swift.struct/allowed.md)**: The model may call tools. This is the default behavior.
- **[`required`](generationoptions/toolcallingmode-swift.struct/required.md)**: The model must call one or more tools before it can respond.
- **[`disallowed`](generationoptions/toolcallingmode-swift.struct/disallowed.md)**: The model can’t call any tools and responds using only its own knowledge.

The following changes the mode from [`required`](generationoptions/toolcallingmode-swift.struct/required.md) to [`allowed`](generationoptions/toolcallingmode-swift.struct/allowed.md) after the first tool call, which lets the model produce a final response:

```swift
extension SessionPropertyValues {
    @SessionPropertyEntry
    var toolCallCount: Int = 0
}

struct RecipeDynamicProfile: LanguageModelSession.DynamicProfile {
    @SessionProperty(\.toolCallCount)
    var toolCallCount
    var body: some LanguageModelSession.DynamicProfile {
        Profile {
            BreadDatabaseTool()
        }
        .toolCallingMode(toolCallCount < 1 ? .required : .allowed)
        .onToolCall {
            toolCallCount += 1
        }
    }
}
```

> ❗ **Important**: When you set the mode to [`required`](generationoptions/toolcallingmode-swift.struct/required.md), you must define an exit condition by either throwing an error from a tool’s [`call(arguments:)`](tool/call(arguments:).md) method or by changing the mode dynamically using a [`LanguageModelSession.DynamicProfile`](languagemodelsession/dynamicprofile.md); otherwise, the model continues to call the tool.

## Topics

### Getting the tool calling modes
- [static let allowed: GenerationOptions.ToolCallingMode](generationoptions/toolcallingmode-swift.struct/allowed.md)
  The model may or may not call tools.
- [static let disallowed: GenerationOptions.ToolCallingMode](generationoptions/toolcallingmode-swift.struct/disallowed.md)
  The model may not call any tool.
- [static let required: GenerationOptions.ToolCallingMode](generationoptions/toolcallingmode-swift.struct/required.md)
  The model must call one or multiple tools.
### Accessing the content
- [var kind: GenerationOptions.ToolCallingMode.Kind](generationoptions/toolcallingmode-swift.struct/kind-swift.property.md)
- [GenerationOptions.ToolCallingMode.Kind](generationoptions/toolcallingmode-swift.struct/kind-swift.enum.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var temperature: Double?](generationoptions/temperature.md)
  A value that influences the confidence of the model’s response.
- [var sampling: GenerationOptions.SamplingMode?](generationoptions/sampling.md)
  A sampling strategy for how the model picks tokens when generating a response.
- [var samplingMode: GenerationOptions.SamplingMode?](generationoptions/samplingmode-swift.property.md)
  A sampling strategy for how the model picks tokens when generating a response.
- [GenerationOptions.SamplingMode](generationoptions/samplingmode-swift.struct.md)
  A type that defines how values are sampled from a probability distribution.
- [var toolCallingMode: GenerationOptions.ToolCallingMode?](generationoptions/toolcallingmode-swift.property.md)
  The tool calling requirements.
- [var maximumResponseTokens: Int?](generationoptions/maximumresponsetokens.md)
  The maximum number of tokens the model is allowed to produce in its response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/toolcallingmode-swift.struct)*