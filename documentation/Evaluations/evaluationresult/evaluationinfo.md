# evaluationInfo

**Framework**: Evaluations  
**Kind**: property

User-defined information about this evaluation, such as the model name, prompt version, or dataset.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
let evaluationInfo: [String : String]
```

## See Also

- [var summary: DataFrame](evaluationresult/summary.md)
  Aggregated statistics for each metric in the evaluation.
- [var detailed: DataFrame](evaluationresult/detailed.md)
  Individual results for each sample in the evaluation.
- [let evaluationID: String](evaluationresult/evaluationid.md)
  The identifier of the evaluation that produced these results.
- [let resultID: UUID](evaluationresult/resultid.md)
  A unique identifier for this particular result.
- [var reportMetadata: [String : any Sendable]](evaluationresult/reportmetadata.md)
  Framework-generated metadata used for report presentation.
- [EvaluationResult.DataFrameKind](evaluationresult/dataframekind.md)
  The kind of DataFrame to convert for JSON serialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationresult/evaluationinfo)*