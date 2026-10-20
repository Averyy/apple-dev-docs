# LanguageModelExecutorGenerationChannel.Usage.Output

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

Token counts for the output produced by the model.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct Output
```

## Topics

### Creating an output instance
- [init(totalTokenCount: Int, reasoningTokenCount: Int)](./output-swift.struct/init%28totaltokencount,reasoningtokencount%29.md)
  Creates output token counts for the response the model produces.
### Handling the output tokens
- [var totalTokenCount: Int](./output-swift.struct/totaltokencount.md)
  The total number of output tokens.
- [var reasoningTokenCount: Int](./output-swift.struct/reasoningtokencount.md)
  The number of output tokens that were part of the model’s reasoning output.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Updating the token counts
- [var input: LanguageModelExecutorGenerationChannel.Usage.Input](./input-swift.property.md)
  The input token counts from the transcript.
- [LanguageModelExecutorGenerationChannel.Usage.Input](./input-swift.struct.md)
  Token counts for the transcript submitted to the model.
- [var output: LanguageModelExecutorGenerationChannel.Usage.Output](./output-swift.property.md)
  The output token counts from the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/usage/output-swift.struct)*