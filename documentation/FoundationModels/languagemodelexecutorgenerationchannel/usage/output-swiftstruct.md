# LanguageModelExecutorGenerationChannel.Usage.Output

**Framework**: Foundation Models  
**Kind**: struct

Token counts for the output produced by the model.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Output
```

## Topics

### Creating an output instance
- [init(totalTokenCount: Int, reasoningTokenCount: Int)](languagemodelexecutorgenerationchannel/usage/output-swift.struct/init(totaltokencount:reasoningtokencount:).md)
### Handling the output tokens
- [var totalTokenCount: Int](languagemodelexecutorgenerationchannel/usage/output-swift.struct/totaltokencount.md)
  The total number of output tokens.
- [var reasoningTokenCount: Int](languagemodelexecutorgenerationchannel/usage/output-swift.struct/reasoningtokencount.md)
  The number of output tokens that were part of the model’s reasoning output.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var input: LanguageModelExecutorGenerationChannel.Usage.Input](languagemodelexecutorgenerationchannel/usage/input-swift.property.md)
  The input token counts from the transcript.
- [LanguageModelExecutorGenerationChannel.Usage.Input](languagemodelexecutorgenerationchannel/usage/input-swift.struct.md)
  Token counts for the transcript submitted to the model.
- [var output: LanguageModelExecutorGenerationChannel.Usage.Output](languagemodelexecutorgenerationchannel/usage/output-swift.property.md)
  The output token counts from the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/usage/output-swift.struct)*