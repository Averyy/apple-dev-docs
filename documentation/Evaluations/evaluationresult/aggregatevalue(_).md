# aggregateValue(_:)

**Framework**: Evaluations  
**Kind**: method  
**Role**: Instance Method

Returns the first aggregate value matching the given operation, or `-1` if not found.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
func aggregateValue(_ operation: AggregationOperation) -> Double
```

## Mentions

- [Evaluating language model responses](../evaluating-language-model-responses.md)

## Parameters

- `operation`: The aggregation operation to match.

## See Also

### Accessing results
- [var summary: DataFrame](./summary.md)
  Aggregated statistics for each metric in the evaluation.
- [var detailed: DataFrame](./detailed.md)
  Individual results for each sample in the evaluation.
- [let evaluationInfo: [String : String]](./evaluationinfo.md)
  User-defined information about this evaluation, such as the model name, prompt version, or dataset.
- [let evaluationID: String](./evaluationid.md)
  The identifier of the evaluation that produced these results.
- [let resultID: UUID](./resultid.md)
  A unique identifier for this particular result.
- [var reportMetadata: [String : any Sendable]](./reportmetadata.md)
  Framework-generated metadata used for report presentation.
- [EvaluationResult.DataFrameKind](./dataframekind.md)
  The kind of DataFrame to convert for JSON serialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationresult/aggregatevalue(_:))*