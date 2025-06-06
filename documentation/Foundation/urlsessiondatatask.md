# URLSessionDataTask

**Framework**: Foundation  
**Kind**: class

A URL session task that returns downloaded data directly to the app in memory.

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
class URLSessionDataTask
```

## Mentions

- [Fetching website data into memory](fetching-website-data-into-memory.md)

#### Overview

A [`URLSessionDataTask`](urlsessiondatatask.md) is a concrete subclass of [`URLSessionTask`](urlsessiontask.md). The methods in the [`URLSessionDataTask`](urlsessiondatatask.md) class are documented in [`URLSessionTask`](urlsessiontask.md).

A data task returns data directly to the app (in memory) as one or more `NSData` objects. When you use a data task:

- During upload of the body data (if your app provides any), the session periodically calls its delegate’s [`urlSession(_:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:)`](urlsessiontaskdelegate/urlsession(_:task:didsendbodydata:totalbytessent:totalbytesexpectedtosend:).md) method with status information.
- After receiving an initial response, the session calls its delegate’s [`urlSession(_:dataTask:didReceive:completionHandler:)`](urlsessiondatadelegate/urlsession(_:datatask:didreceive:completionhandler:).md) method to let you examine the status code and headers, and optionally convert the data task into a download task.
- During the transfer, the session calls its delegate’s [`urlSession(_:dataTask:didReceive:)`](urlsessiondatadelegate/urlsession(_:datatask:didreceive:).md) method to provide your app with the content as it arrives.
- Upon completion, the session calls its delegate’s [`urlSession(_:dataTask:willCacheResponse:completionHandler:)`](urlsessiondatadelegate/urlsession(_:datatask:willcacheresponse:completionhandler:).md) method to let you determine whether the response should be cached.

For examples of using data tasks for fetching and uploading data, see [`Fetching website data into memory`](fetching-website-data-into-memory.md) and [`Uploading data to a website`](uploading-data-to-a-website.md).

## Topics

### Initializers
- [init()](urlsessiondatatask/init.md)
### Type Methods
- [class func new() -> Self](urlsessiondatatask/new.md)

## Relationships

### Inherits From
- [URLSessionTask](urlsessiontask.md)
### Inherited By
- [URLSessionUploadTask](urlsessionuploadtask.md)
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

## See Also

- [func dataTask(with: URL) -> URLSessionDataTask](urlsession/datatask(with:)-10dy7.md)
  Creates a task that retrieves the contents of the specified URL.
- [func dataTask(with: URL, completionHandler: (Data?, URLResponse?, (any Error)?) -> Void) -> URLSessionDataTask](urlsession/datatask(with:completionhandler:)-52wk8.md)
  Creates a task that retrieves the contents of the specified URL, then calls a handler upon completion.
- [func dataTask(with: URLRequest) -> URLSessionDataTask](urlsession/datatask(with:)-7jpys.md)
  Creates a task that retrieves the contents of a URL based on the specified URL request object.
- [func dataTask(with: URLRequest, completionHandler: (Data?, URLResponse?, (any Error)?) -> Void) -> URLSessionDataTask](urlsession/datatask(with:completionhandler:)-e6xv.md)
  Creates a task that retrieves the contents of a URL based on the specified URL request object, and calls a handler upon completion.
- [protocol URLSessionDataDelegate](urlsessiondatadelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to data and upload tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiondatatask)*