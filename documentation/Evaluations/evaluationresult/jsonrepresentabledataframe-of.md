# jsonRepresentableDataFrame(of:)

**Framework**: Evaluations  
**Kind**: method

Transforms a DataFrame into one with column types compatible with JSON representation.

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
func jsonRepresentableDataFrame(of kind: EvaluationResult.DataFrameKind) throws -> DataFrame
```

#### Return Value

A new DataFrame with JSON-serializable column types.

#### Discussion

The detailed branch always excludes the `Transcript` column from this public helper; transcript serialization is opted into through [`jsonData(includeReportMetadata:includeTranscripts:jsonOptions:)`](evaluationresult/jsondata(includereportmetadata:includetranscripts:jsonoptions:).md).

## Parameters

- `kind`: Whether to convert the summary or detailed DataFrame.

## See Also

- [var groupedSummary: String](evaluationresult/groupedsummary.md)
  A formatted description of summary metrics organized by groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationresult/jsonrepresentabledataframe(of:))*