# EvaluationResult

**Framework**: Evaluations  
**Kind**: struct

The results of running a model evaluation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct EvaluationResult
```

## Mentions

- [Designing effective evaluations](designing-effective-evaluations.md)
- [Evaluating language model responses](evaluating-language-model-responses.md)

#### Overview

A structure that contains the summary and detailed results from an evaluation run.

## Topics

### Accessing results
- [var summary: DataFrame](evaluationresult/summary.md)
  Aggregated statistics for each metric in the evaluation.
- [var detailed: DataFrame](evaluationresult/detailed.md)
  Individual results for each sample in the evaluation.
- [let evaluationInfo: [String : String]](evaluationresult/evaluationinfo.md)
  User-defined information about this evaluation, such as the model name, prompt version, or dataset.
- [let evaluationID: String](evaluationresult/evaluationid.md)
  The identifier of the evaluation that produced these results.
- [let resultID: UUID](evaluationresult/resultid.md)
  A unique identifier for this particular result.
- [var reportMetadata: [String : any Sendable]](evaluationresult/reportmetadata.md)
  Framework-generated metadata used for report presentation.
- [func aggregateValue(AggregationOperation) -> Double](evaluationresult/aggregatevalue(_:).md)
  Returns the first aggregate value matching the given operation, or `-1` if not found.
- [EvaluationResult.DataFrameKind](evaluationresult/dataframekind.md)
  The kind of DataFrame to convert for JSON serialization.
### Inspecting timing
- [let startTime: Date](evaluationresult/starttime.md)
  The time when the evaluation run started.
- [let endTime: Date](evaluationresult/endtime.md)
  The time when the evaluation run finished.
- [var duration: TimeInterval](evaluationresult/duration.md)
  The total duration of the evaluation run.
### Formatting results
- [var groupedSummary: String](evaluationresult/groupedsummary.md)
  A formatted description of summary metrics organized by groups.
- [func jsonRepresentableDataFrame(of: EvaluationResult.DataFrameKind) throws -> DataFrame](evaluationresult/jsonrepresentabledataframe(of:).md)
  Transforms a DataFrame into one with column types compatible with JSON representation.
### Saving and loading results
- [func saveJSON(to: URL, includeReportMetadata: Bool) throws -> URL](evaluationresult/savejson(to:includereportmetadata:).md)
  Saves evaluation results to a single JSON file.
- [func jsonData(includeReportMetadata: Bool, jsonOptions: JSONSerialization.WritingOptions) throws -> Data](evaluationresult/jsondata(includereportmetadata:jsonoptions:).md)
  Returns the evaluation results as JSON data.
- [static func loadJSON(from: URL) throws -> EvaluationResult](evaluationresult/loadjson(from:).md)
  Loads an evaluation result from a JSON file on disk.
- [static func loadJSONLines(from: URL) async throws -> [EvaluationResult]](evaluationresult/loadjsonlines(from:).md)
  Loads an array of evaluation results from a JSONL file on disk.
- [init(jsonData: Data) throws](evaluationresult/init(jsondata:).md)
  Creates an evaluation result by parsing JSON data.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ResultColumn](resultcolumn.md)
  A typed descriptor for a column in an evaluation result DataFrame.
- [var inputColumn: ResultColumn<Self.Sample>](evaluation/inputcolumn.md)
  A typed column descriptor for the input samples in the detailed DataFrame.
- [var responseColumn: ResultColumn<Self.Subject>](evaluation/responsecolumn.md)
  A typed column descriptor for the model responses in the detailed DataFrame.
- [var expectedColumn: ResultColumn<Self.Sample.ExpectedValue>](evaluation/expectedcolumn.md)
  A typed column descriptor for the expected values in the detailed DataFrame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationresult)*