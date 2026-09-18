# LanguageModelSession.Usage.Input

**Framework**: Foundation Models  
**Kind**: struct

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

### Creating a token input instance
- [init(totalTokenCount: Int, cachedTokenCount: Int)](languagemodelsession/usage-swift.struct/input-swift.struct/init(totaltokencount:cachedtokencount:).md)
  Creates an input token count.
### Getting the token count
- [var cachedTokenCount: Int](languagemodelsession/usage-swift.struct/input-swift.struct/cachedtokencount.md)
  The number of input tokens that were served from a cache.
- [var totalTokenCount: Int](languagemodelsession/usage-swift.struct/input-swift.struct/totaltokencount.md)
  The total number of input tokens from the transcript.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var input: LanguageModelSession.Usage.Input](languagemodelsession/usage-swift.struct/input-swift.property.md)
  The input token counts from the transcript.
- [var output: LanguageModelSession.Usage.Output](languagemodelsession/usage-swift.struct/output-swift.property.md)
  The output token counts from the response.
- [LanguageModelSession.Usage.Output](languagemodelsession/usage-swift.struct/output-swift.struct.md)
  Token counts for the output produced by the model.
- [var metadata: [String : GeneratedContent]](languagemodelsession/usage-swift.struct/metadata.md)
  Additional usage statistics that the language model encodes for the response.
- [var totalTokenCount: Int](languagemodelsession/usage-swift.struct/totaltokencount.md)
  The total number of tokens involved in this generation, combining input and output counts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/usage-swift.struct/input-swift.struct)*