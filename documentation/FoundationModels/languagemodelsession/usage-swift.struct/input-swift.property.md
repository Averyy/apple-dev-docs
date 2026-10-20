# input

**Framework**: Foundation Models  
**Kind**: property  
**Role**: Instance Property

The input token counts from the transcript.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var input: LanguageModelSession.Usage.Input
```

## See Also

### Updating the usage
- [LanguageModelSession.Usage.Input](./input-swift.struct.md)
  Token counts for the transcript submitted to the model.
- [var output: LanguageModelSession.Usage.Output](./output-swift.property.md)
  The output token counts from the response.
- [LanguageModelSession.Usage.Output](./output-swift.struct.md)
  Token counts for the output produced by the model.
- [var metadata: [String : GeneratedContent]](./metadata.md)
  Additional usage statistics that the language model encodes for the response.
- [var totalTokenCount: Int](./totaltokencount.md)
  The total number of tokens involved in this generation, combining input and output counts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/usage-swift.struct/input-swift.property)*