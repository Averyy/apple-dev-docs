# metadata

**Framework**: Foundation Models  
**Kind**: property

Language models that provide other kinds of usage statistics may encode them in metadata.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var metadata: [String : any Sendable & Codable & Equatable]
```

## See Also

- [var input: LanguageModelSession.Usage.Input](languagemodelsession/usage-swift.struct/input-swift.property.md)
  The input token counts from the transcript.
- [LanguageModelSession.Usage.Input](languagemodelsession/usage-swift.struct/input-swift.struct.md)
  Token counts for the transcript submitted to the model.
- [var output: LanguageModelSession.Usage.Output](languagemodelsession/usage-swift.struct/output-swift.property.md)
  The output token counts from the response.
- [LanguageModelSession.Usage.Output](languagemodelsession/usage-swift.struct/output-swift.struct.md)
  Token counts for the output produced by the model.
- [var totalTokenCount: Int](languagemodelsession/usage-swift.struct/totaltokencount.md)
  The total number of tokens involved in this generation, equal to `input.totalTokenCount + output.totalTokenCount`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/usage-swift.struct/metadata)*