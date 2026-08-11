# jsonData(includeReportMetadata:includeTranscripts:jsonOptions:)

**Framework**: Evaluations  
**Kind**: method

Returns the evaluation results as JSON data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func jsonData(includeReportMetadata: Bool = false, includeTranscripts: Bool = false, jsonOptions: JSONSerialization.WritingOptions = [.prettyPrinted, .sortedKeys]) throws -> Data
```

#### Return Value

The JSON representation of the evaluation results as `Data`.

#### Discussion

The data contains sections for summary, results, metadata, and optionally report metadata.

## Parameters

- `includeReportMetadata`: Whether to include report metadata. Defaults to `false`.
- `includeTranscripts`: Whether to encode each row’s transcript into the `Transcript` column as JSON. Defaults to `false` to keep file size small for runs that don’t need transcripts in the artifact.
- `jsonOptions`: The writing options for the final JSON serialization. Defaults to `[.prettyPrinted, .sortedKeys]`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationresult/jsondata(includereportmetadata:includetranscripts:jsonoptions:))*