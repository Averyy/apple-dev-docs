# file(contentType:destinationDirectory:)

**Framework**: App Intents  
**Kind**: method

Requests an `IntentFile` representation as a file url.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func file(contentType: UTType, destinationDirectory: URL? = nil) async throws -> (fileURL: URL, openedInPlace: Bool)
```

#### Discussion

If a destination directory is not given the file is opened in place, falling back to a temporary directory if this fails. If the file is not opened in place and a destination directory is used it is the caller’s responsibility to remove the file.

## Parameters

- `contentType`: A content type of the returned data.
- `destinationDirectory`: The directory the file should be copied to,   if no directory is provided the file is opened in place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentfile/file(contenttype:destinationdirectory:))*