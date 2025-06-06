# URLSessionTaskDelegate

**Framework**: Foundation  
**Kind**: protocol

A protocol that defines methods that URL session instances call on their delegates to handle task-level events.

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
protocol URLSessionTaskDelegate : URLSessionDelegate
```

## Mentions

- [Uploading streams of data](uploading-streams-of-data.md)
- [Fetching website data into memory](fetching-website-data-into-memory.md)
- [Downloading files from websites](downloading-files-from-websites.md)
- [Uploading data to a website](uploading-data-to-a-website.md)

#### Overview

You use this protocol in one of two ways, depending on how you use a [`URLSession`](urlsession.md):

- If you create tasks with Swift’s `async`-`await` syntax, using methods like [`bytes(for:delegate:)`](urlsession/bytes(for:delegate:).md) and [`data(for:delegate:)`](urlsession/data(for:delegate:).md), you pass a `delegate` argument of this type. The delegate receives callbacks for things like task progress, while the call point awaits the completion of the task.
- If you add tasks to the session with methods like [`dataTask(with:)`](urlsession/datatask(with:)-10dy7.md) and [`downloadTask(with:)`](urlsession/downloadtask(with:)-1onj.md), then you implement this protocol’s methods in a [`delegate`](urlsession/delegate.md) you set on the session. This session delegate may also implement other protocols as appropriate, like [`URLSessionDownloadDelegate`](urlsessiondownloaddelegate.md) and [`URLSessionDataDelegate`](urlsessiondatadelegate.md). You can also assign a delegate of this type directly to the task to intercept callbacks before the task delivers them to the session’s delegate.

> **Note**:  Your [`URLSession`](urlsession.md) object doesn’t need to have a delegate. If you don’t assign a delegate, the session uses a system-provided delegate. In this case, you must provide a completion callback or use the Swift `async`-`await` methods to obtain the data.

## Topics

### Handling task life cycle changes
- [func urlSession(URLSession, task: URLSessionTask, didCompleteWithError: (any Error)?)](urlsessiontaskdelegate/urlsession(_:task:didcompletewitherror:).md)
  Tells the delegate that the task finished transferring data.
### Handling redirects
- [func urlSession(URLSession, task: URLSessionTask, willPerformHTTPRedirection: HTTPURLResponse, newRequest: URLRequest, completionHandler: (URLRequest?) -> Void)](urlsessiontaskdelegate/urlsession(_:task:willperformhttpredirection:newrequest:completionhandler:).md)
  Tells the delegate that the remote server requested an HTTP redirect.
### Working with upload tasks
- [func urlSession(URLSession, task: URLSessionTask, didSendBodyData: Int64, totalBytesSent: Int64, totalBytesExpectedToSend: Int64)](urlsessiontaskdelegate/urlsession(_:task:didsendbodydata:totalbytessent:totalbytesexpectedtosend:).md)
  Periodically informs the delegate of the progress of sending body content to the server.
- [func urlSession(URLSession, task: URLSessionTask, needNewBodyStream: (InputStream?) -> Void)](urlsessiontaskdelegate/urlsession(_:task:neednewbodystream:).md)
  Tells the delegate when a task requires a new request body stream to send to the remote server.
### Handling authentication challenges
- [func urlSession(URLSession, task: URLSessionTask, didReceive: URLAuthenticationChallenge, completionHandler: (URLSession.AuthChallengeDisposition, URLCredential?) -> Void)](urlsessiontaskdelegate/urlsession(_:task:didreceive:completionhandler:).md)
  Requests credentials from the delegate in response to an authentication request from the remote server.
- [URLSession.AuthChallengeDisposition](urlsession/authchallengedisposition.md)
  Constants passed by session or task delegates to the provided continuation block in response to an authentication challenge.
### Handling delayed and waiting tasks
- [func urlSession(URLSession, task: URLSessionTask, willBeginDelayedRequest: URLRequest, completionHandler: (URLSession.DelayedRequestDisposition, URLRequest?) -> Void)](urlsessiontaskdelegate/urlsession(_:task:willbegindelayedrequest:completionhandler:).md)
  Tells the delegate that a delayed URL session task will now begin loading.
- [URLSession.DelayedRequestDisposition](urlsession/delayedrequestdisposition.md)
  The action to take on a delayed URL session task.
- [func urlSession(URLSession, taskIsWaitingForConnectivity: URLSessionTask)](urlsessiontaskdelegate/urlsession(_:taskiswaitingforconnectivity:).md)
  Tells the delegate that the task is waiting until suitable connectivity is available before beginning the network load.
### Collecting task metrics
- [func urlSession(URLSession, task: URLSessionTask, didFinishCollecting: URLSessionTaskMetrics)](urlsessiontaskdelegate/urlsession(_:task:didfinishcollecting:).md)
  Tells the delegate that the session finished collecting metrics for the task.
- [class URLSessionTaskMetrics](urlsessiontaskmetrics.md)
  An object encapsulating the metrics for a session task.
### Instance Methods
- [func urlSession(URLSession, didCreateTask: URLSessionTask)](urlsessiontaskdelegate/urlsession(_:didcreatetask:).md)
- [func urlSession(URLSession, task: URLSessionTask, didReceiveInformationalResponse: HTTPURLResponse)](urlsessiontaskdelegate/urlsession(_:task:didreceiveinformationalresponse:).md)
- [func urlSession(URLSession, task: URLSessionTask, needNewBodyStreamFrom: Int64, completionHandler: (InputStream?) -> Void)](urlsessiontaskdelegate/urlsession(_:task:neednewbodystreamfrom:completionhandler:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [URLSessionDelegate](urlsessiondelegate.md)
### Inherited By
- [URLSessionDataDelegate](urlsessiondatadelegate.md)
- [URLSessionDownloadDelegate](urlsessiondownloaddelegate.md)
- [URLSessionStreamDelegate](urlsessionstreamdelegate.md)
- [URLSessionWebSocketDelegate](urlsessionwebsocketdelegate.md)

## See Also

- [var delegate: (any URLSessionDelegate)?](urlsession/delegate.md)
  The delegate assigned when this object was created.
- [protocol URLSessionDelegate](urlsessiondelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle session-level events, like session life cycle changes.
- [var delegateQueue: OperationQueue](urlsession/delegatequeue.md)
  The operation queue provided when this object was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Foundation/urlsessiontaskdelegate)*