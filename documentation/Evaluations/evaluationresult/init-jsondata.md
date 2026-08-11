# init(jsonData:)

**Framework**: Evaluations  
**Kind**: init

Creates an evaluation result by parsing JSON data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(jsonData data: Data) throws
```

## Parameters

- `data`: The JSON data to parse.

## See Also

- [static func loadJSON(from: URL) throws -> EvaluationResult](evaluationresult/loadjson(from:).md)
  Loads an evaluation result from a JSON file on disk.
- [static func loadJSONLines(from: URL) async throws -> [EvaluationResult]](evaluationresult/loadjsonlines(from:).md)
  Loads an array of evaluation results from a JSONL file on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationresult/init(jsondata:))*