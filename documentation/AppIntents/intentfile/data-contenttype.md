# data(contentType:)

**Framework**: App Intents  
**Kind**: method

Requests an `IntentFile` representation as binary data of the requested content type if possible.

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
func data(contentType: UTType) async throws -> Data
```

#### Discussion

If the `IntentFile` is backed by a file `URL`, this might cause loading the entire file contents into memory.

## Parameters

- `contentType`: A content type of the returned data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentfile/data(contenttype:))*