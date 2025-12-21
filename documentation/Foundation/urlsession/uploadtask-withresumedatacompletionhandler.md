# uploadTask(withResumeData:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Creates a URLSessionUploadTask from a resume data blob. If resuming from an upload file, the file must still exist and be unmodified.

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
func uploadTask(withResumeData resumeData: Data, completionHandler: @escaping (Data?, URLResponse?, (any Error)?) -> Void) -> URLSessionUploadTask
```

#### Return Value

A new session upload task, or nil if the resumeData is invalid.

## Parameters

- `resumeData`: Resume data blob from an incomplete upload, such as data returned by the cancelByProducingResumeData: method.
- `completionHandler`: The completion handler to call when the load request is complete.

## See Also

- [Building a resumable upload server with SwiftNIO](building-a-resumable-upload-server-with-swiftnio.md)
  Support HTTP resumable upload protocol in SwiftNIO by translating resumable uploads to regular uploads.
- [func uploadTask(with: URLRequest, from: Data) -> URLSessionUploadTask](urlsession/uploadtask(with:from:).md)
  Creates a task that performs an HTTP request for the specified URL request object and uploads the provided data.
- [func uploadTask(with: URLRequest, from: Data?, completionHandler: (Data?, URLResponse?, (any Error)?) -> Void) -> URLSessionUploadTask](urlsession/uploadtask(with:from:completionhandler:).md)
  Creates a task that performs an HTTP request for the specified URL request object, uploads the provided data, and calls a handler upon completion.
- [func uploadTask(with: URLRequest, fromFile: URL) -> URLSessionUploadTask](urlsession/uploadtask(with:fromfile:).md)
  Creates a task that performs an HTTP request for uploading the specified file.
- [func uploadTask(with: URLRequest, fromFile: URL, completionHandler: (Data?, URLResponse?, (any Error)?) -> Void) -> URLSessionUploadTask](urlsession/uploadtask(with:fromfile:completionhandler:).md)
  Creates a task that performs an HTTP request for uploading the specified file, then calls a handler upon completion.
- [func uploadTask(withStreamedRequest: URLRequest) -> URLSessionUploadTask](urlsession/uploadtask(withstreamedrequest:).md)
  Creates a task that performs an HTTP request for uploading data based on the specified URL request.
- [func uploadTask(withResumeData: Data) -> URLSessionUploadTask](urlsession/uploadtask(withresumedata:).md)
  Creates an upload task from a resume data blob. Requires the server to support the latest resumable uploads Internet-Draft from the HTTP Working Group, found at https://datatracker.ietf.org/doc/draft-ietf-httpbis-resumable-upload/ If resuming from an upload file, the file must still exist and be unmodified. If the upload cannot be successfully resumed, URLSession:task:didCompleteWithError: will be called.
- [class URLSessionUploadTask](urlsessionuploadtask.md)
  A URL session task that uploads data to the network in a request body.
- [protocol URLSessionDataDelegate](urlsessiondatadelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to data and upload tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/uploadtask(withresumedata:completionhandler:))*