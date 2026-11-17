# EvaluationResult.DataFrameKind

**Framework**: Evaluations  
**Kind**: enum  
**Role**: Enumeration

The kind of data frame to convert for JSON serialization.

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
enum DataFrameKind
```

## Overview

An [`EvaluationResult`](../evaluationresult.md) holds two [`DataFrame`](../../TabularData/dataframe.md) values: an aggregated [`summary`](./summary.md) and a per-sample [`detailed`](./detailed.md) data frame. Pass a value of this type to [`jsonRepresentableDataFrame(of:)`](./jsonrepresentabledataframe%28of%29.md) to choose which of the two to convert.

```swift
let kind: EvaluationResult.DataFrameKind = .summary
```

## Topics

### Enumeration Cases
- [EvaluationResult.DataFrameKind.detailed](./dataframekind/detailed.md)
  The sample-level detailed results data frame.
- [EvaluationResult.DataFrameKind.summary](./dataframekind/summary.md)
  The aggregated summary data frame.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

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
- [func aggregateValue(AggregationOperation) -> Double](./aggregatevalue%28_%29.md)
  Returns the first aggregate value matching the given operation, or `-1` if not found.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationresult/dataframekind)*