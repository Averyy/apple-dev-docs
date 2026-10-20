# GenerationOptions.ToolCallingMode

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A value that describes how the model uses tools.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct ToolCallingMode
```

## Mentions

- [Expanding generation with tool calling](../expanding-generation-with-tool-calling.md)

#### Overview

Use this to control how the model interacts with tools for a given request. Tool calling mode supports three modes:

- **[`allowed`](./toolcallingmode-swift.struct/allowed.md)**: The model may call tools. This is the default behavior.
- **[`required`](./toolcallingmode-swift.struct/required.md)**: The model must call one or more tools before it can respond.
- **[`disallowed`](./toolcallingmode-swift.struct/disallowed.md)**: The model can’t call any tools and responds using only its own knowledge.

The following changes the mode from [`required`](./toolcallingmode-swift.struct/required.md) to [`allowed`](./toolcallingmode-swift.struct/allowed.md) after the first tool call, which lets the model produce a final response:

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

> ❗ **Important**: When you set the mode to [`required`](./toolcallingmode-swift.struct/required.md), you must define an exit condition by either throwing an error from a tool’s [`call(arguments:)`](../tool/call%28arguments%29.md) method or by changing the mode dynamically using a [`LanguageModelSession.DynamicProfile`](../languagemodelsession/dynamicprofile.md); otherwise, the model continues to call the tool.

## Topics

### Getting the tool calling modes
- [static let allowed: GenerationOptions.ToolCallingMode](./toolcallingmode-swift.struct/allowed.md)
  The model may or may not call tools.
- [static let disallowed: GenerationOptions.ToolCallingMode](./toolcallingmode-swift.struct/disallowed.md)
  The model may not call any tool.
- [static let required: GenerationOptions.ToolCallingMode](./toolcallingmode-swift.struct/required.md)
  The model must call one or multiple tools.
### Accessing the content
- [var kind: GenerationOptions.ToolCallingMode.Kind](./toolcallingmode-swift.struct/kind-swift.property.md)
  The tool-calling behavior this mode represents.
- [GenerationOptions.ToolCallingMode.Kind](./toolcallingmode-swift.struct/kind-swift.enum.md)
  A representation of the different ways a model can use tools.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring options
- [var temperature: Double?](./temperature.md)
  A value that influences the confidence of the model’s response.
- [var sampling: GenerationOptions.SamplingMode?](./sampling.md)
  A sampling strategy for how the model picks tokens when generating a response.
- [var samplingMode: GenerationOptions.SamplingMode?](./samplingmode-swift.property.md)
  A sampling strategy for how the model picks tokens when generating a response.
- [GenerationOptions.SamplingMode](./samplingmode-swift.struct.md)
  A type that defines how values are sampled from a probability distribution.
- [var toolCallingMode: GenerationOptions.ToolCallingMode?](./toolcallingmode-swift.property.md)
  The tool calling requirements.
- [var maximumResponseTokens: Int?](./maximumresponsetokens.md)
  The maximum number of tokens the model is allowed to produce in its response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/toolcallingmode-swift.struct)*