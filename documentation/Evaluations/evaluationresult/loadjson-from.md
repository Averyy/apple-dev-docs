# loadJSON(from:)

**Framework**: Evaluations  
**Kind**: method

Loads an evaluation result from a JSON file on disk.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func loadJSON(from url: URL) throws -> EvaluationResult
```

#### Return Value

The deserialized [`EvaluationResult`](evaluationresult.md).

## Parameters

- `url`: The file URL from which to read the JSON data.

## See Also

- [func saveJSON(to: URL, includeReportMetadata: Bool) throws -> URL](evaluationresult/savejson(to:includereportmetadata:).md)
  Saves evaluation results to a single JSON file.
- [func jsonData(includeReportMetadata: Bool, jsonOptions: JSONSerialization.WritingOptions) throws -> Data](evaluationresult/jsondata(includereportmetadata:jsonoptions:).md)
  Returns the evaluation results as JSON data.
- [static func loadJSONLines(from: URL) async throws -> [EvaluationResult]](evaluationresult/loadjsonlines(from:).md)
  Loads an array of evaluation results from a JSONL file on disk.
- [init(jsonData: Data) throws](evaluationresult/init(jsondata:).md)
  Creates an evaluation result by parsing JSON data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationresult/loadjson(from:))*