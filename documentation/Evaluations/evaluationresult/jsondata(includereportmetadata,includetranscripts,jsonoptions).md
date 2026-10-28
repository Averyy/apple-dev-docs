# jsonData(includeReportMetadata:includeTranscripts:jsonOptions:)

**Framework**: Evaluations  
**Kind**: method  
**Role**: Instance Method

Returns the evaluation results as JSON data.

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
func jsonData(includeReportMetadata: Bool = false, includeTranscripts: Bool = false, jsonOptions: JSONSerialization.WritingOptions = [.prettyPrinted, .sortedKeys]) throws -> Data
```

## Return Value

The JSON representation of the evaluation results as `Data`.

## Discussion

The data contains sections for summary, results, metadata, and optionally report metadata.

## Parameters

- `includeReportMetadata`: Whether to include report metadata. Defaults to `false`.
- `includeTranscripts`: Whether to encode each row’s transcript into the `Transcript` column as JSON. Defaults to `false` to keep file size small for runs that don’t need transcripts in the artifact.
- `jsonOptions`: The writing options for the final JSON serialization. Defaults to `[.prettyPrinted, .sortedKeys]`.

## See Also

### Saving and loading results
- [func saveJSON(to: URL, includeReportMetadata: Bool, includeTranscripts: Bool) throws -> URL](./savejson%28to,includereportmetadata,includetranscripts%29.md)
  Saves evaluation results to a single JSON file.
- [static func loadJSON(from: URL) throws -> EvaluationResult](./loadjson%28from%29.md)
  Loads an evaluation result from a JSON file on disk.
- [static func loadJSONLines(from: URL) async throws -> [EvaluationResult]](./loadjsonlines%28from%29.md)
  Loads an array of evaluation results from a JSONL file on disk.
- [init(jsonData: Data) throws](./init%28jsondata%29.md)
  Creates an evaluation result by parsing JSON data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationresult/jsondata(includereportmetadata:includetranscripts:jsonoptions:))*