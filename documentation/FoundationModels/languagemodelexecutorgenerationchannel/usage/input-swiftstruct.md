# LanguageModelExecutorGenerationChannel.Usage.Input

**Framework**: Foundation Models  
**Kind**: struct

Token counts for the transcript submitted to the model.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Input
```

## Topics

### Creating an input instance
- [init(totalTokenCount: Int, cachedTokenCount: Int)](languagemodelexecutorgenerationchannel/usage/input-swift.struct/init(totaltokencount:cachedtokencount:).md)
### Handling the input tokens
- [var totalTokenCount: Int](languagemodelexecutorgenerationchannel/usage/input-swift.struct/totaltokencount.md)
  The total number of input tokens from the transcript.
- [var cachedTokenCount: Int](languagemodelexecutorgenerationchannel/usage/input-swift.struct/cachedtokencount.md)
  The number of input tokens that were served from a cache.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var input: LanguageModelExecutorGenerationChannel.Usage.Input](languagemodelexecutorgenerationchannel/usage/input-swift.property.md)
  The input token counts from the transcript.
- [var output: LanguageModelExecutorGenerationChannel.Usage.Output](languagemodelexecutorgenerationchannel/usage/output-swift.property.md)
  The output token counts from the response.
- [LanguageModelExecutorGenerationChannel.Usage.Output](languagemodelexecutorgenerationchannel/usage/output-swift.struct.md)
  Token counts for the output produced by the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/usage/input-swift.struct)*