# uploadTask(with:from:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Creates a task that performs an HTTP request for the specified URL request object, uploads the provided data, and calls a handler upon completion.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func uploadTask(with request: URLRequest, from bodyData: Data?, completionHandler: @escaping (Data?, URLResponse?, (any Error)?) -> Void) -> URLSessionUploadTask
```

## Mentions

- [Uploading data to a website](uploading-data-to-a-website.md)

#### Return Value

The new session upload task.

#### Discussion

An HTTP upload request is any request that contains a request body, such as a `POST` or `PUT` request. Upload tasks require you to create a request object so that you can provide metadata for the upload, like HTTP request headers.

Unlike [`uploadTask(with:from:)`](urlsession/uploadtask(with:from:).md), this method returns the response body after it has been received in full, and does not require you to write a custom delegate to obtain the response body.

By using a completion handler, the task bypasses calls to delegate methods for response and data delivery, and instead provides any resulting data, response, or error inside the completion handler. Delegate methods for handling authentication challenges, however, are still called.

Typically you pass a `nil` completion handler only when creating tasks in sessions whose delegates include a [`urlSession(_:dataTask:didReceive:)`](urlsessiondatadelegate/urlsession(_:datatask:didreceive:).md) method. However, if you do not need the response data, use key-value observing to watch for changes to the task’s status to determine when it completes.

After you create the task, you must start it by calling its [`resume()`](urlsessiontask/resume().md) method.

If the request completes successfully, the `data` parameter of the completion handler block contains the resource data, and the `error` parameter is `nil`. If the request fails, the `data` parameter is `nil,` and the `error` parameter contains information about the failure. If a response from the server is received, regardless of whether the request completes successfully or fails, the `response` parameter contains that information.

## Parameters

- `request`: A URL request object that provides the URL, cache policy, request type, and so on. The body stream and body data in this request object are ignored.
- `bodyData`: The body data for the request.
- `completionHandler`: This completion handler takes the following parameters:

## See Also

- [Building a resumable upload server with SwiftNIO](building-a-resumable-upload-server-with-swiftnio.md)
  Support HTTP resumable upload protocol in SwiftNIO by translating resumable uploads to regular uploads.
- [func uploadTask(with: URLRequest, from: Data) -> URLSessionUploadTask](urlsession/uploadtask(with:from:).md)
  Creates a task that performs an HTTP request for the specified URL request object and uploads the provided data.
- [func uploadTask(with: URLRequest, fromFile: URL) -> URLSessionUploadTask](urlsession/uploadtask(with:fromfile:).md)
  Creates a task that performs an HTTP request for uploading the specified file.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/uploadtask(with:from:completionhandler:))*