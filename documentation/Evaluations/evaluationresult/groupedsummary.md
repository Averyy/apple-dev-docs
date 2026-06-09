# groupedSummary

**Framework**: Evaluations  
**Kind**: property

A formatted description of summary metrics organized by groups.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var groupedSummary: String { get }
```

## Mentions

- [Evaluating language model responses](evaluating-language-model-responses.md)

#### Example Output

```swift
Text Matching:
  Correct (%): 0.75
  First Word Correct (%): 0.83

Text Quality:
  Ratio of Match Length: 0.92
  Length Distribution: 0.014
```

## See Also

- [func jsonRepresentableDataFrame(of: EvaluationResult.DataFrameKind) throws -> DataFrame](evaluationresult/jsonrepresentabledataframe(of:).md)
  Transforms a DataFrame into one with column types compatible with JSON representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationresult/groupedsummary)*