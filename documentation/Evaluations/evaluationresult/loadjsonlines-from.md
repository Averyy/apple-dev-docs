# loadJSONLines(from:)

**Framework**: Evaluations  
**Kind**: method

Loads an array of evaluation results from a JSONL file on disk.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) static func loadJSONLines(from url: URL) async throws -> [EvaluationResult]
```

#### Return Value

An array of [`EvaluationResult`](evaluationresult.md).

#### Discussion

Each line in the file is expected to be a valid JSON object representing an evaluation result.

## Parameters

- `url`: The file URL to read the JSONL data from.

## See Also

- [func saveJSON(to: URL, includeReportMetadata: Bool) throws -> URL](evaluationresult/savejson(to:includereportmetadata:).md)
  Saves evaluation results to a single JSON file.
- [func jsonData(includeReportMetadata: Bool, jsonOptions: JSONSerialization.WritingOptions) throws -> Data](evaluationresult/jsondata(includereportmetadata:jsonoptions:).md)
  Returns the evaluation results as JSON data.
- [static func loadJSON(from: URL) throws -> EvaluationResult](evaluationresult/loadjson(from:).md)
  Loads an evaluation result from a JSON file on disk.
- [init(jsonData: Data) throws](evaluationresult/init(jsondata:).md)
  Creates an evaluation result by parsing JSON data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationresult/loadjsonlines(from:))*