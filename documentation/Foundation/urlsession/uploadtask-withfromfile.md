# uploadTask(with:fromFile:)

**Framework**: Foundation  
**Kind**: method

Creates a task that performs an HTTP request for uploading the specified file.

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
func uploadTask(with request: URLRequest, fromFile fileURL: URL) -> URLSessionUploadTask
```

#### Return Value

The new session upload task.

#### Discussion

An HTTP upload request is any request that contains a request body, such as a `POST` or `PUT` request. Upload tasks require you to create a request object so that you can provide metadata for the upload, like HTTP request headers.

After you create the task, you must start it by calling its [`resume()`](urlsessiontask/resume().md) method. The task calls methods on the session’s delegate to provide you with the upload’s progress, response metadata, response data, and so on.

## Parameters

- `request`: A URL request object that provides the URL, cache policy, request type, and so on. The body stream and body data in this request object are ignored.
- `fileURL`: The URL of the file to upload.

## See Also

- [Building a resumable upload server with SwiftNIO](building-a-resumable-upload-server-with-swiftnio.md)
  Support HTTP resumable upload protocol in SwiftNIO by translating resumable uploads to regular uploads.
- [func uploadTask(with: URLRequest, from: Data) -> URLSessionUploadTask](urlsession/uploadtask(with:from:).md)
  Creates a task that performs an HTTP request for the specified URL request object and uploads the provided data.
- [func uploadTask(with: URLRequest, from: Data?, completionHandler: (Data?, URLResponse?, (any Error)?) -> Void) -> URLSessionUploadTask](urlsession/uploadtask(with:from:completionhandler:).md)
  Creates a task that performs an HTTP request for the specified URL request object, uploads the provided data, and calls a handler upon completion.
- [func uploadTask(with: URLRequest, fromFile: URL, completionHandler: (Data?, URLResponse?, (any Error)?) -> Void) -> URLSessionUploadTask](urlsession/uploadtask(with:fromfile:completionhandler:).md)
  Creates a task that performs an HTTP request for uploading the specified file, then calls a handler upon completion.
- [func uploadTask(withStreamedRequest: URLRequest) -> URLSessionUploadTask](urlsession/uploadtask(withstreamedrequest:).md)
  Creates a task that performs an HTTP request for uploading data based on the specified URL request.
- [func uploadTask(withResumeData: Data) -> URLSessionUploadTask](urlsession/uploadtask(withresumedata:).md)
  Creates an upload task from a resume data blob. Requires the server to support the latest resumable uploads Internet-Draft from the HTTP Working Group, found at https://datatracker.ietf.org/doc/draft-ietf-httpbis-resumable-upload/ If resuming from an upload file, the file must still exist and be unmodified. If the upload cannot be successfully resumed, URLSession:task:didCompleteWithError: will be called.
- [func uploadTask(withResumeData: Data, completionHandler: (Data?, URLResponse?, (any Error)?) -> Void) -> URLSessionUploadTask](urlsession/uploadtask(withresumedata:completionhandler:).md)
  Creates a URLSessionUploadTask from a resume data blob. If resuming from an upload file, the file must still exist and be unmodified.
- [class URLSessionUploadTask](urlsessionuploadtask.md)
  A URL session task that uploads data to the network in a request body.
- [protocol URLSessionDataDelegate](urlsessiondatadelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to data and upload tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/uploadtask(with:fromfile:))*