# EvaluationResult

**Framework**: Evaluations  
**Kind**: struct  
**Role**: Structure

The results of running a model evaluation.

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
struct EvaluationResult
```

## Mentions

- [Evaluating language model responses](./evaluating-language-model-responses.md)
- [Designing effective evaluations](./designing-effective-evaluations.md)

#### Overview

A structure that contains the summary and detailed results from an evaluation run.

Use the column descriptors from your [`Evaluation`](./evaluation.md) to access typed columns from the [`detailed`](./evaluationresult/detailed.md) DataFrame:

```swift
let result = try await evaluation.run(on: samples)
let inputs = result.detailed[evaluation.inputColumn]
let responses = result.detailed[evaluation.responseColumn]
let expected = result.detailed[evaluation.expectedColumn]
```

## Topics

### Accessing results
- [var summary: DataFrame](./evaluationresult/summary.md)
  Aggregated statistics for each metric in the evaluation.
- [var detailed: DataFrame](./evaluationresult/detailed.md)
  Individual results for each sample in the evaluation.
- [let evaluationInfo: [String : String]](./evaluationresult/evaluationinfo.md)
  User-defined information about this evaluation, such as the model name, prompt version, or dataset.
- [let evaluationID: String](./evaluationresult/evaluationid.md)
  The identifier of the evaluation that produced these results.
- [let resultID: UUID](./evaluationresult/resultid.md)
  A unique identifier for this particular result.
- [var reportMetadata: [String : any Sendable]](./evaluationresult/reportmetadata.md)
  Framework-generated metadata used for report presentation.
- [func aggregateValue(AggregationOperation) -> Double](./evaluationresult/aggregatevalue%28_%29.md)
  Returns the first aggregate value matching the given operation, or `-1` if not found.
- [EvaluationResult.DataFrameKind](./evaluationresult/dataframekind.md)
  The kind of DataFrame to convert for JSON serialization.
### Inspecting timing
- [let startTime: Date](./evaluationresult/starttime.md)
  The time when the evaluation run started.
- [let endTime: Date](./evaluationresult/endtime.md)
  The time when the evaluation run finished.
- [var duration: TimeInterval](./evaluationresult/duration.md)
  The total duration of the evaluation run.
### Formatting results
- [var groupedSummary: String](./evaluationresult/groupedsummary.md)
  A formatted description of summary metrics organized by groups.
- [func jsonRepresentableDataFrame(of: EvaluationResult.DataFrameKind) throws -> DataFrame](./evaluationresult/jsonrepresentabledataframe%28of%29.md)
  Transforms a DataFrame into one with column types compatible with JSON representation.
### Saving and loading results
- [func saveJSON(to: URL, includeReportMetadata: Bool, includeTranscripts: Bool) throws -> URL](./evaluationresult/savejson%28to,includereportmetadata,includetranscripts%29.md)
  Saves evaluation results to a single JSON file.
- [func jsonData(includeReportMetadata: Bool, includeTranscripts: Bool, jsonOptions: JSONSerialization.WritingOptions) throws -> Data](./evaluationresult/jsondata%28includereportmetadata,includetranscripts,jsonoptions%29.md)
  Returns the evaluation results as JSON data.
- [static func loadJSON(from: URL) throws -> EvaluationResult](./evaluationresult/loadjson%28from%29.md)
  Loads an evaluation result from a JSON file on disk.
- [static func loadJSONLines(from: URL) async throws -> [EvaluationResult]](./evaluationresult/loadjsonlines%28from%29.md)
  Loads an array of evaluation results from a JSONL file on disk.
- [init(jsonData: Data) throws](./evaluationresult/init%28jsondata%29.md)
  Creates an evaluation result by parsing JSON data.
### Instance Properties
- [let errors: EvaluationRunErrors](./evaluationresult/errors.md)
  A summary of the failures encountered during the run.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Results
- [struct ResultColumn](./resultcolumn.md)
  A typed descriptor for a column in an evaluation result DataFrame.
- [var inputColumn: ResultColumn<Self.Sample>](./evaluation/inputcolumn.md)
  A typed column descriptor for the input samples in the detailed DataFrame.
- [var responseColumn: ResultColumn<Self.Subject>](./evaluation/responsecolumn.md)
  A typed column descriptor for the model responses in the detailed DataFrame.
- [var expectedColumn: ResultColumn<Self.Sample.ExpectedValue>](./evaluation/expectedcolumn.md)
  A typed column descriptor for the expected values in the detailed DataFrame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationresult)*