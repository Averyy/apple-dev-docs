# cancel(byProducingResumeData:)

**Framework**: Foundation  
**Kind**: method

Cancels a download and calls a callback with resume data for later use.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func cancelByProducingResumeData() async -> Data?
```

## Mentions

- [Pausing and resuming downloads](pausing-and-resuming-downloads.md)
- [Pausing and resuming uploads](pausing-and-resuming-uploads.md)

#### Discussion

A download can be resumed only if the following conditions are met:

- The resource has not changed since you first requested it
- The task is an HTTP or HTTPS `GET` request
- The server provides either the `ETag` or `Last-Modified` header (or both) in its response
- The server supports byte-range requests
- The temporary file hasn’t been deleted by the system in response to disk space pressure

## Parameters

- `completionHandler`: This block is not guaranteed to execute in a particular thread context. As such, you may want specify an appropriate dispatch queue in which to perform any work.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiondownloadtask/cancel(byproducingresumedata:))*