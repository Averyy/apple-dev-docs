# cancel(byProducingResumeData:)

**Framework**: Foundation  
**Kind**: method

Cancels an upload and calls the completion handler with resume data for later use. resumeData will be nil if the server does not support the latest resumable uploads Internet-Draft from the HTTP Working Group, found at https://datatracker.ietf.org/doc/draft-ietf-httpbis-resumable-upload/

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func cancelByProducingResumeData() async -> Data?
```

## Parameters

- `completionHandler`: The completion handler to call when the upload has been successfully canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionuploadtask/cancel(byproducingresumedata:))*