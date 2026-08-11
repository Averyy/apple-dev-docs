# LanguageModelSession.Usage.Output

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

### Creating a token output instance
- [init(totalTokenCount: Int, reasoningTokenCount: Int)](languagemodelsession/usage-swift.struct/output-swift.struct/init(totaltokencount:reasoningtokencount:).md)
  Creates an output token count.
### Getting the token count
- [var reasoningTokenCount: Int](languagemodelsession/usage-swift.struct/output-swift.struct/reasoningtokencount.md)
  The number of output tokens that were part of the model’s reasoning output.
- [var totalTokenCount: Int](languagemodelsession/usage-swift.struct/output-swift.struct/totaltokencount.md)
  The total number of output tokens.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var input: LanguageModelSession.Usage.Input](languagemodelsession/usage-swift.struct/input-swift.property.md)
  The input token counts from the transcript.
- [LanguageModelSession.Usage.Input](languagemodelsession/usage-swift.struct/input-swift.struct.md)
  Token counts for the transcript submitted to the model.
- [var output: LanguageModelSession.Usage.Output](languagemodelsession/usage-swift.struct/output-swift.property.md)
  The output token counts from the response.
- [var metadata: [String : GeneratedContent]](languagemodelsession/usage-swift.struct/metadata.md)
  Language models that provide other kinds of usage statistics may encode them in metadata.
- [var totalTokenCount: Int](languagemodelsession/usage-swift.struct/totaltokencount.md)
  The total number of tokens involved in this generation, combining input and output counts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/usage-swift.struct/output-swift.struct)*