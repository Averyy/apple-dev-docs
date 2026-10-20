# LanguageModelExecutorGenerationChannel.Usage.Input

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

Token counts for the transcript submitted to the model.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct Input
```

## Topics

### Creating an input instance
- [init(totalTokenCount: Int, cachedTokenCount: Int)](./input-swift.struct/init%28totaltokencount,cachedtokencount%29.md)
  Creates input token counts for the transcript submitted to the model.
### Handling the input tokens
- [var totalTokenCount: Int](./input-swift.struct/totaltokencount.md)
  The total number of input tokens from the transcript.
- [var cachedTokenCount: Int](./input-swift.struct/cachedtokencount.md)
  The number of input tokens that were served from a cache.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Updating the token counts
- [var input: LanguageModelExecutorGenerationChannel.Usage.Input](./input-swift.property.md)
  The input token counts from the transcript.
- [var output: LanguageModelExecutorGenerationChannel.Usage.Output](./output-swift.property.md)
  The output token counts from the response.
- [LanguageModelExecutorGenerationChannel.Usage.Output](./output-swift.struct.md)
  Token counts for the output produced by the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/usage/input-swift.struct)*