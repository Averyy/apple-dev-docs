# saveJSONLines(to:includeReportMetadata:)

**Framework**: Swift  
**Kind**: method

Saves the array of evaluation results as a JSONL file

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
func saveJSONLines(to url: URL, includeReportMetadata: Bool = false) throws -> URL
```

#### Return Value

The URL of the saved file.

## Parameters

- `url`: The file URL to write the JSONL output to.
- `includeReportMetadata`: Whether to include report metadata in each entry. Defaults to `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collection/savejsonlines(to:includereportmetadata:))*