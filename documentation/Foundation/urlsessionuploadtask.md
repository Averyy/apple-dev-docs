# URLSessionUploadTask

**Framework**: Foundation  
**Kind**: class

A URL session task that uploads data to the network in a request body.

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
class URLSessionUploadTask
```

## Mentions

- [Pausing and resuming uploads](pausing-and-resuming-uploads.md)
- [Uploading streams of data](uploading-streams-of-data.md)
- [Uploading data to a website](uploading-data-to-a-website.md)

#### Overview

The [`URLSessionUploadTask`](urlsessionuploadtask.md) class is a subclass of [`URLSessionDataTask`](urlsessiondatatask.md), which in turn is a concrete subclass of [`URLSessionTask`](urlsessiontask.md). The methods associated with the [`URLSessionUploadTask`](urlsessionuploadtask.md) class are documented in [`URLSessionTask`](urlsessiontask.md).

Upload tasks are used for making HTTP requests that require a request body (such as `POST` or `PUT`). They behave similarly to data tasks, but you create them by calling different methods on the session that are designed to make it easier to provide the content to upload. As with data tasks, if the server provides a response, upload tasks return that response as one or more `NSData` objects in memory.

> **Note**:  Unlike data tasks, you can use upload tasks to upload content in the background.

When you create an upload task, you provide a [`URLRequest`](urlrequest.md) instance that contains any additional headers that you might need to send alongside the upload, such as the content type, content disposition, and so on. In iOS, when you create an upload task for a file in a background session, the system copies that file to a temporary location and streams data from there.

While the upload is in progress, the task calls the session delegate’s [`urlSession(_:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:)`](urlsessiontaskdelegate/urlsession(_:task:didsendbodydata:totalbytessent:totalbytesexpectedtosend:).md) method periodically to provide you with status information.

When the upload phase of the request finishes, the task behaves like a data task, calling methods on the session delegate to provide you with the server’s response—headers, status code, content data, and so on.

## Topics

### Initializers
- [init()](urlsessionuploadtask/init.md)
### Instance Methods
- [func cancel(byProducingResumeData: (Data?) -> Void)](urlsessionuploadtask/cancel(byproducingresumedata:).md)
### Type Methods
- [class func new() -> Self](urlsessionuploadtask/new.md)

## Relationships

### Inherits From
- [URLSessionDataTask](urlsessiondatatask.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [ProgressReporting](progressreporting.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [func uploadTask(withResumeData: Data, completionHandler: (Data?, URLResponse?, (any Error)?) -> Void) -> URLSessionUploadTask](urlsession/uploadtask(withresumedata:completionhandler:).md)
- [protocol URLSessionDataDelegate](urlsessiondatadelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to data and upload tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionuploadtask)*