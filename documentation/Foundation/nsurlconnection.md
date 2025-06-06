# NSURLConnection

**Framework**: Foundation  
**Kind**: class

An object that enables you to start and stop URL requests.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSURLConnection
```

#### Overview

> ❗ **Important**:  This API is considered legacy. Use [`URLSession`](urlsession.md) instead.

An `NSURLConnection` object lets you load the contents of a URL by providing a URL request object. The interface for `NSURLConnection` is sparse, providing only the controls to start and cancel asynchronous loads of a URL request. You perform most of your configuration on the URL request object itself.

> **Note**:  Although instances of this class are commonly called “connections”, there is not a 1:1 correlation between these objects and the underlying network connections.

The `NSURLConnection` class provides convenience class methods to load URL requests both asynchronously using a callback block and synchronously.

For greater control, you can create a URL connection object with a delegate object that conforms to the [`NSURLConnectionDelegate`](nsurlconnectiondelegate.md) and [`NSURLConnectionDataDelegate`](nsurlconnectiondatadelegate.md) protocols. The connection calls methods on that delegate to provide you with progress and status as the URL request is loaded asynchronously. The connection also calls delegate methods to let you override the connection’s default behavior (for example, specifying how a particular redirect should be handled). These delegate methods are called on the thread that initiated the asynchronous load operation.

> **Note**:  During a request, the connection maintains a strong reference to its delegate. It releases that strong reference when the connection finishes loading, fails, or is canceled.

For more information about errors, see the `NSURLError.h` header, [`Foundation Constants`](foundation-constants.md), and URL Loading System Error Codes in [`Error Handling Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ErrorHandlingCocoa/ErrorHandling/ErrorHandling.html#//apple_ref/doc/uid/TP40001806).

##### Nsurlconnection Protocols

The `NSURLConnection` class works in tandem with three formal protocols: [`NSURLConnectionDelegate`](nsurlconnectiondelegate.md), [`NSURLConnectionDataDelegate`](nsurlconnectiondatadelegate.md), and [`NSURLConnectionDownloadDelegate`](nsurlconnectiondownloaddelegate.md). To use these protocols, you write a class that conforms to them and implement any methods that are appropriate, then provide an instance of that class as the delegate when you create a connection object.

The [`NSURLConnectionDelegate`](nsurlconnectiondelegate.md) protocol is primarily used for credential handling, but also handles connection completion. Because it handles connection failure during data transfers, all connection delegates must typically implement this protocol.

In addition, unless you’re using Newsstand Kit, your delegate must also conform to the [`NSURLConnectionDataDelegate`](nsurlconnectiondatadelegate.md) protocol, because this protocol provides methods that the `NSURLConnection` class calls with progress information during an upload, with fragments of the response data during a download, and to provide a new upload body stream if the server’s response necessitates a second connection attempt—for example, if `NSURLConnection` must retry the request with different credentials.

Finally, if you’re using Newsstand Kit, your delegate can conform to the [`NSURLConnectionDownloadDelegate`](nsurlconnectiondownloaddelegate.md) protocol. This protocol provides support for continuing interrupted file downloads and receiving a notification whenever a download finishes. This protocol is solely for use with `NSURLConnection` objects created using Newsstand Kit’s `download(with:)` method.

> **Note**:  Some methods in these protocols were previously part of other formal protocols or were previously part of an informal protocol on `NSObject`.

## Topics

### Preflighting a Connection Request
- [class func canHandle(URLRequest) -> Bool](nsurlconnection/canhandle(_:).md)
  Returns whether a request can be handled based on a preflight evaluation.
### Connection URL Information
- [var originalRequest: URLRequest](nsurlconnection/originalrequest.md)
  A deep copy of the original connection request.
- [var currentRequest: URLRequest](nsurlconnection/currentrequest.md)
  The current connection request.
### Loading Data Synchronously
- [class func sendSynchronousRequest(URLRequest, returning: AutoreleasingUnsafeMutablePointer<URLResponse?>?) throws -> Data](nsurlconnection/sendsynchronousrequest(_:returning:).md)
  Performs a synchronous load of the specified URL request.
### Loading Data Asynchronously
- [init?(request: URLRequest, delegate: Any?)](nsurlconnection/init(request:delegate:).md)
  Returns an initialized URL connection and begins to load the data for the URL request.
- [init?(request: URLRequest, delegate: Any?, startImmediately: Bool)](nsurlconnection/init(request:delegate:startimmediately:).md)
  Returns an initialized URL connection and begins to load the data for the URL request, if specified.
- [class func sendAsynchronousRequest(URLRequest, queue: OperationQueue, completionHandler: (URLResponse?, Data?, (any Error)?) -> Void)](nsurlconnection/sendasynchronousrequest(_:queue:completionhandler:).md)
  Loads the data for a URL request and executes a handler block on an operation queue when the request completes or fails.
- [func start()](nsurlconnection/start.md)
  Causes the connection to begin loading data, if it has not already.
### Stopping a Connection
- [func cancel()](nsurlconnection/cancel.md)
  Cancels an asynchronous load of a request.
### Scheduling Delegate Method Calls
- [func schedule(in: RunLoop, forMode: RunLoop.Mode)](nsurlconnection/schedule(in:formode:).md)
  Determines the run loop and mode that the connection uses to call methods on its delegate.
- [func setDelegateQueue(OperationQueue?)](nsurlconnection/setdelegatequeue(_:).md)
  Determines the operation queue that is used to call methods on the connection’s delegate.
- [func unschedule(from: RunLoop, forMode: RunLoop.Mode)](nsurlconnection/unschedule(from:formode:).md)
  Causes the connection to stop calling delegate methods in the specified run loop and mode.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSURLConnectionDelegate](nsurlconnectiondelegate.md)
  A protocol that delegates of a URL connection implement to receive status about and provide feedback to the connection object.
- [protocol NSURLConnectionDataDelegate](nsurlconnectiondatadelegate.md)
  A protocol that most delegates of a URL connection implement to receive data associated with the connection.
- [protocol NSURLConnectionDownloadDelegate](nsurlconnectiondownloaddelegate.md)
  A protocol that delegates of a URL connection created with Newsstand Kit implement to receive data associated with a download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Foundation/nsurlconnection)*