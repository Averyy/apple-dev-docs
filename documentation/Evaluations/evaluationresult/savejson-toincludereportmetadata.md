# saveJSON(to:includeReportMetadata:)

**Framework**: Evaluations  
**Kind**: method

Saves evaluation results to a single JSON file.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@discardableResult
func saveJSON(to directory: URL, includeReportMetadata: Bool = false) throws -> URL
```

#### Return Value

The URL of the saved file

#### Discussion

The file contains sections for summary, results, metadata, and optionally report metadata.

## Parameters

- `directory`: The directory to save the file in.
- `includeReportMetadata`: Whether to include report metadata. Defaults to `false`.

## See Also

- [func jsonData(includeReportMetadata: Bool, jsonOptions: JSONSerialization.WritingOptions) throws -> Data](evaluationresult/jsondata(includereportmetadata:jsonoptions:).md)
  Returns the evaluation results as JSON data.
- [static func loadJSON(from: URL) throws -> EvaluationResult](evaluationresult/loadjson(from:).md)
  Loads an evaluation result from a JSON file on disk.
- [static func loadJSONLines(from: URL) async throws -> [EvaluationResult]](evaluationresult/loadjsonlines(from:).md)
  Loads an array of evaluation results from a JSONL file on disk.
- [init(jsonData: Data) throws](evaluationresult/init(jsondata:).md)
  Creates an evaluation result by parsing JSON data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationresult/savejson(to:includereportmetadata:))*