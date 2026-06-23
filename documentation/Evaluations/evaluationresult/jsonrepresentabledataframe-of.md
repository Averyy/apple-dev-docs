# jsonRepresentableDataFrame(of:)

**Framework**: Evaluations  
**Kind**: method

Transforms a DataFrame into one with column types compatible with JSON representation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func jsonRepresentableDataFrame(of kind: EvaluationResult.DataFrameKind) throws -> DataFrame
```

#### Return Value

A new DataFrame with JSON-serializable column types.

## Parameters

- `kind`: Whether to convert the summary or detailed DataFrame.

## See Also

- [var groupedSummary: String](evaluationresult/groupedsummary.md)
  A formatted description of summary metrics organized by groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationresult/jsonrepresentabledataframe(of:))*