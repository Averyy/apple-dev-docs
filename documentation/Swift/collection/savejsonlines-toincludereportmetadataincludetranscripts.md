# saveJSONLines(to:includeReportMetadata:includeTranscripts:)

**Framework**: Swift  
**Kind**: method

Saves the array of evaluation results as a JSONL file

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@discardableResult
func saveJSONLines(to url: URL, includeReportMetadata: Bool = false, includeTranscripts: Bool = false) throws -> URL
```

#### Return Value

The URL of the saved file.

## Parameters

- `url`: The file URL to write the JSONL output to.
- `includeReportMetadata`: Whether to include report metadata in each entry. Defaults to `false`.
- `includeTranscripts`: Whether to encode each row’s transcript into the `Transcript` column of each entry as JSON. Defaults to `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collection/savejsonlines(to:includereportmetadata:includetranscripts:))*