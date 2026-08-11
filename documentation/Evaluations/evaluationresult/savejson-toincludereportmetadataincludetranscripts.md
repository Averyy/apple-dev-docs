# saveJSON(to:includeReportMetadata:includeTranscripts:)

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
func saveJSON(to directory: URL, includeReportMetadata: Bool = false, includeTranscripts: Bool = false) throws -> URL
```

#### Return Value

The URL of the saved file

#### Discussion

The file contains sections for summary, results, metadata, and optionally report metadata.

## Parameters

- `directory`: The directory to save the file in.
- `includeReportMetadata`: Whether to include report metadata. Defaults to `false`.
- `includeTranscripts`: Whether to encode each row’s transcript into the `Transcript` column as JSON. Defaults to `false`. Enable when you want a saved file that carries transcripts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationresult/savejson(to:includereportmetadata:includetranscripts:))*