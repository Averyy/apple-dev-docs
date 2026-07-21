# LanguageModelSession.Usage.Input

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var input: LanguageModelSession.Usage.Input](languagemodelsession/usage-swift.struct/input-swift.property.md)
  The input token counts from the transcript.
- [var output: LanguageModelSession.Usage.Output](languagemodelsession/usage-swift.struct/output-swift.property.md)
  The output token counts from the response.
- [LanguageModelSession.Usage.Output](languagemodelsession/usage-swift.struct/output-swift.struct.md)
  Token counts for the output produced by the model.
- [var metadata: [String : any Sendable]](languagemodelsession/usage-swift.struct/metadata.md)
  Language models that provide other kinds of usage statistics may encode them in metadata.
- [var totalTokenCount: Int](languagemodelsession/usage-swift.struct/totaltokencount.md)
  The total number of tokens involved in this generation, equal to `input.totalTokenCount + output.totalTokenCount`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/usage-swift.struct/input-swift.struct)*