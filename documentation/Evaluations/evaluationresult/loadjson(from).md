# loadJSON(from:)

**Framework**: Evaluations  
**Kind**: method  
**Role**: Type Method

Loads an evaluation result from a JSON file on disk.

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
static func loadJSON(from url: URL) throws -> EvaluationResult
```

## Return Value

The deserialized [`EvaluationResult`](../evaluationresult.md).

## Parameters

- `url`: The file URL from which to read the JSON data.

## See Also

### Saving and loading results
- [func saveJSON(to: URL, includeReportMetadata: Bool, includeTranscripts: Bool) throws -> URL](./savejson%28to,includereportmetadata,includetranscripts%29.md)
  Saves evaluation results to a single JSON file.
- [func jsonData(includeReportMetadata: Bool, includeTranscripts: Bool, jsonOptions: JSONSerialization.WritingOptions) throws -> Data](./jsondata%28includereportmetadata,includetranscripts,jsonoptions%29.md)
  Returns the evaluation results as JSON data.
- [static func loadJSONLines(from: URL) async throws -> [EvaluationResult]](./loadjsonlines%28from%29.md)
  Loads an array of evaluation results from a JSONL file on disk.
- [init(jsonData: Data) throws](./init%28jsondata%29.md)
  Creates an evaluation result by parsing JSON data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationresult/loadjson(from:))*