# URLSessionTaskDelegate

**Framework**: Foundation  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol NSURLSessionTaskDelegate <NSURLSessionDelegate>
```

## Mentions

- [Uploading streams of data](./uploading-streams-of-data.md)
- [Downloading files from websites](./downloading-files-from-websites.md)
- [Fetching website data into memory](./fetching-website-data-into-memory.md)
- [Uploading data to a website](./uploading-data-to-a-website.md)

#### Overview

You use this protocol in one of two ways, depending on how you use a [`URLSession`](./urlsession.md):

- If you create tasks with Swift’s `async`-`await` syntax, using methods like [`bytes(for:delegate:)`](./urlsession/bytes%28for,delegate%29.md) and [`data(for:delegate:)`](./urlsession/data%28for,delegate%29.md), you pass a `delegate` argument of this type. The delegate receives callbacks for things like task progress, while the call point awaits the completion of the task.
- If you add tasks to the session with methods like [`dataTask(with:)`](./urlsession/datatask%28with%29-10dy7.md) and [`downloadTask(with:)`](./urlsession/downloadtask%28with%29-1onj.md), then you implement this protocol’s methods in a [`delegate`](./urlsession/delegate.md) you set on the session. This session delegate may also implement other protocols as appropriate, like [`URLSessionDownloadDelegate`](./urlsessiondownloaddelegate.md) and [`URLSessionDataDelegate`](./urlsessiondatadelegate.md). You can also assign a delegate of this type directly to the task to intercept callbacks before the task delivers them to the session’s delegate.

> **Note**:  Your [`URLSession`](./urlsession.md) object doesn’t need to have a delegate. If you don’t assign a delegate, the session uses a system-provided delegate. In this case, you must provide a completion callback or use the Swift `async`-`await` methods to obtain the data.

## Topics

### Handling task life cycle changes
- [func urlSession(URLSession, task: URLSessionTask, didCompleteWithError: (any Error)?)](./urlsessiontaskdelegate/urlsession%28_,task,didcompletewitherror%29.md)
  Tells the delegate that the task finished transferring data.
### Handling redirects
- [func urlSession(URLSession, task: URLSessionTask, willPerformHTTPRedirection: HTTPURLResponse, newRequest: URLRequest, completionHandler: (URLRequest?) -> Void)](./urlsessiontaskdelegate/urlsession%28_,task,willperformhttpredirection,newrequest,completionhandler%29.md)
  Tells the delegate that the remote server requested an HTTP redirect.
### Working with upload tasks
- [func urlSession(URLSession, task: URLSessionTask, didSendBodyData: Int64, totalBytesSent: Int64, totalBytesExpectedToSend: Int64)](./urlsessiontaskdelegate/urlsession%28_,task,didsendbodydata,totalbytessent,totalbytesexpectedtosend%29.md)
  Periodically informs the delegate of the progress of sending body content to the server.
- [func urlSession(URLSession, task: URLSessionTask, needNewBodyStream: (InputStream?) -> Void)](./urlsessiontaskdelegate/urlsession%28_,task,neednewbodystream%29.md)
  Tells the delegate when a task requires a new request body stream to send to the remote server.
### Handling authentication challenges
- [func urlSession(URLSession, task: URLSessionTask, didReceive: URLAuthenticationChallenge, completionHandler: (URLSession.AuthChallengeDisposition, URLCredential?) -> Void)](./urlsessiontaskdelegate/urlsession%28_,task,didreceive,completionhandler%29.md)
  Requests credentials from the delegate in response to an authentication request from the remote server.
- [URLSession.AuthChallengeDisposition](./urlsession/authchallengedisposition.md)
  Constants passed by session or task delegates to the provided continuation block in response to an authentication challenge.
### Handling delayed and waiting tasks
- [func urlSession(URLSession, task: URLSessionTask, willBeginDelayedRequest: URLRequest, completionHandler: (URLSession.DelayedRequestDisposition, URLRequest?) -> Void)](./urlsessiontaskdelegate/urlsession%28_,task,willbegindelayedrequest,completionhandler%29.md)
  Tells the delegate that a delayed URL session task will now begin loading.
- [URLSession.DelayedRequestDisposition](./urlsession/delayedrequestdisposition.md)
  The action to take on a delayed URL session task.
- [func urlSession(URLSession, taskIsWaitingForConnectivity: URLSessionTask)](./urlsessiontaskdelegate/urlsession%28_,taskiswaitingforconnectivity%29.md)
  Tells the delegate that the task is waiting until suitable connectivity is available before beginning the network load.
### Collecting task metrics
- [func urlSession(URLSession, task: URLSessionTask, didFinishCollecting: URLSessionTaskMetrics)](./urlsessiontaskdelegate/urlsession%28_,task,didfinishcollecting%29.md)
  Tells the delegate that the session finished collecting metrics for the task.
- [class URLSessionTaskMetrics](./urlsessiontaskmetrics.md)
  An object encapsulating the metrics for a session task.
### Instance Methods
- [func urlSession(URLSession, didCreateTask: URLSessionTask)](./urlsessiontaskdelegate/urlsession%28_,didcreatetask%29.md)
- [func urlSession(URLSession, task: URLSessionTask, didReceiveInformationalResponse: HTTPURLResponse)](./urlsessiontaskdelegate/urlsession%28_,task,didreceiveinformationalresponse%29.md)
- [func urlSession(URLSession, task: URLSessionTask, needNewBodyStreamFrom: Int64, completionHandler: (InputStream?) -> Void)](./urlsessiontaskdelegate/urlsession%28_,task,neednewbodystreamfrom,completionhandler%29.md)
  Tells the delegate if a task requires a new body stream starting from the given offset. This may be necessary when resuming a failed upload task.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [URLSessionDelegate](./urlsessiondelegate.md)
### Inherited By
- [URLSessionDataDelegate](./urlsessiondatadelegate.md)
- [URLSessionDownloadDelegate](./urlsessiondownloaddelegate.md)
- [URLSessionStreamDelegate](./urlsessionstreamdelegate.md)
- [URLSessionWebSocketDelegate](./urlsessionwebsocketdelegate.md)

## See Also

### Working with a delegate
- [var delegate: (any URLSessionDelegate)?](./urlsession/delegate.md)
  The delegate assigned when this object was created.
- [protocol URLSessionDelegate](./urlsessiondelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle session-level events, like session life cycle changes.
- [var delegateQueue: OperationQueue](./urlsession/delegatequeue.md)
  The operation queue provided when this object was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate)*