# jsonData(includeReportMetadata:jsonOptions:)

**Framework**: Evaluations  
**Kind**: method

Returns the evaluation results as JSON data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func jsonData(includeReportMetadata: Bool = false, jsonOptions: JSONSerialization.WritingOptions = [.prettyPrinted, .sortedKeys]) throws -> Data
```

#### Return Value

The JSON representation of the evaluation results as `Data`.

#### Discussion

The data contains sections for summary, results, metadata, and optionally report metadata.

## Parameters

- `includeReportMetadata`: Whether to include report metadata. Defaults to `false`.
- `jsonOptions`: The writing options for the final JSON serialization. Defaults to `[.prettyPrinted, .sortedKeys]`.

## See Also

- [func saveJSON(to: URL, includeReportMetadata: Bool) throws -> URL](evaluationresult/savejson(to:includereportmetadata:).md)
  Saves evaluation results to a single JSON file.
- [static func loadJSON(from: URL) throws -> EvaluationResult](evaluationresult/loadjson(from:).md)
  Loads an evaluation result from a JSON file on disk.
- [static func loadJSONLines(from: URL) async throws -> [EvaluationResult]](evaluationresult/loadjsonlines(from:).md)
  Loads an array of evaluation results from a JSONL file on disk.
- [init(jsonData: Data) throws](evaluationresult/init(jsondata:).md)
  Creates an evaluation result by parsing JSON data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationresult/jsondata(includereportmetadata:jsonoptions:))*