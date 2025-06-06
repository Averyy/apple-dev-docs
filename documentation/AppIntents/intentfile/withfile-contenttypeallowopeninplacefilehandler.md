# withFile(contentType:allowOpenInPlace:fileHandler:)

**Framework**: App Intents  
**Kind**: method

Requests an `IntentFile` representation as a file url.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func withFile<Result>(contentType: UTType, allowOpenInPlace: Bool = false, fileHandler: @escaping (URL, Bool) async throws -> Result) async throws -> Result
```

#### Discussion

If the file is not opened in place, the system removes it after the fileHandler closure returns.

```swift
let image = try await intentFile.withFile(contentType: .png) { url, _ in
    let data = try Data(contentsOf: url)
    return CGImage(pngData: data)
}
```

## Parameters

- `contentType`: A content type of the returned data.
- `allowOpenInPlace`: Whether the file should be opened in place, if possible.
- `fileHandler`: A closure that accepts the file URL as a parameter.   The file is written to a temporary destination and removed   right after the closure returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentfile/withfile(contenttype:allowopeninplace:filehandler:))*