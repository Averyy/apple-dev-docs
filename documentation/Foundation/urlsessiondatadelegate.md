# URLSessionDataDelegate

**Framework**: Foundation  
**Kind**: protocol

A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to data and upload tasks.

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
protocol URLSessionDataDelegate : URLSessionTaskDelegate
```

## Mentions

- [Fetching website data into memory](fetching-website-data-into-memory.md)
- [Accessing cached data](accessing-cached-data.md)

#### Overview

Your session delegate should also implement the methods in the [`URLSessionTaskDelegate`](urlsessiontaskdelegate.md) protocol to handle task-level events that are common to all task types, and methods in the [`URLSessionDelegate`](urlsessiondelegate.md) protocol to handle session-level events.

> **Note**:  A [`URLSession`](urlsession.md) object need not have a delegate. If no delegate is assigned, when you create tasks in that session, you must provide a completion handler block to obtain the data. Completion handler blocks are primarily intended as an alternative to using a custom delegate. If you create a task using a method that takes a completion handler block, the delegate methods for response and data delivery are not called.

## Topics

### Handling task life cycle changes
- [func urlSession(URLSession, dataTask: URLSessionDataTask, didReceive: URLResponse, completionHandler: (URLSession.ResponseDisposition) -> Void)](urlsessiondatadelegate/urlsession(_:datatask:didreceive:completionhandler:).md)
  Tells the delegate that the data task received the initial reply (headers) from the server.
- [URLSession.ResponseDisposition](urlsession/responsedisposition.md)
  Constants indicating how a data or upload session should proceed after receiving the initial headers.
- [func urlSession(URLSession, dataTask: URLSessionDataTask, didBecome: URLSessionDownloadTask)](urlsessiondatadelegate/urlsession(_:datatask:didbecome:)-60op5.md)
  Tells the delegate that the data task was changed to a download task.
- [func urlSession(URLSession, dataTask: URLSessionDataTask, didBecome: URLSessionStreamTask)](urlsessiondatadelegate/urlsession(_:datatask:didbecome:)-7nqzu.md)
  Tells the delegate that the data task was changed to a stream task.
### Receiving data
- [func urlSession(URLSession, dataTask: URLSessionDataTask, didReceive: Data)](urlsessiondatadelegate/urlsession(_:datatask:didreceive:).md)
  Tells the delegate that the data task has received some of the expected data.
### Handling caching
- [func urlSession(URLSession, dataTask: URLSessionDataTask, willCacheResponse: CachedURLResponse, completionHandler: (CachedURLResponse?) -> Void)](urlsessiondatadelegate/urlsession(_:datatask:willcacheresponse:completionhandler:).md)
  Asks the delegate whether the data (or upload) task should store the response in the cache.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [URLSessionDelegate](urlsessiondelegate.md)
- [URLSessionTaskDelegate](urlsessiontaskdelegate.md)

## See Also

- [func dataTask(with: URL) -> URLSessionDataTask](urlsession/datatask(with:)-10dy7.md)
  Creates a task that retrieves the contents of the specified URL.
- [func dataTask(with: URL, completionHandler: (Data?, URLResponse?, (any Error)?) -> Void) -> URLSessionDataTask](urlsession/datatask(with:completionhandler:)-52wk8.md)
  Creates a task that retrieves the contents of the specified URL, then calls a handler upon completion.
- [func dataTask(with: URLRequest) -> URLSessionDataTask](urlsession/datatask(with:)-7jpys.md)
  Creates a task that retrieves the contents of a URL based on the specified URL request object.
- [func dataTask(with: URLRequest, completionHandler: (Data?, URLResponse?, (any Error)?) -> Void) -> URLSessionDataTask](urlsession/datatask(with:completionhandler:)-e6xv.md)
  Creates a task that retrieves the contents of a URL based on the specified URL request object, and calls a handler upon completion.
- [class URLSessionDataTask](urlsessiondatatask.md)
  A URL session task that returns downloaded data directly to the app in memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate)*