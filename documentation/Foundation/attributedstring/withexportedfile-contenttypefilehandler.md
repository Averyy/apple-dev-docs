# withExportedFile(contentType:fileHandler:)

**Framework**: Foundation  
**Kind**: method

Using the type’s `Transferable` conformance implementation, exports a value by writing it to disk and removes when not needed.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
func withExportedFile<Result>(contentType: UTType?, fileHandler: (URL) async throws -> Result) async throws -> Result
```

#### Discussion

This converts a `Transferable` item into a temporary file, and removes it after `fileHandler` closure returns. The default implementation of this function is available to all types that conform to `Transferable` protocol.

## Parameters

- `contentType`: A content type of the requested file.   If the content type is not provided, CoreTransferable creates   a file from the first   that supports export.
- `fileHandler`: A closure that accepts a file URL as a parameter.   The file is written to a temporary destination and removed   after the closure returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/withexportedfile(contenttype:filehandler:))*