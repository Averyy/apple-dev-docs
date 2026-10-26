# start()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Causes the connection to begin loading data, if it has not already.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func start()
```

```objc
- (void) start;
```

#### Discussion

Calling this method is necessary only if you create a connection with the [`init(request:delegate:startImmediately:)`](./init%28request,delegate,startimmediately%29.md) method and provide [`false`](../../Swift/false.md) for the `startImmediately` parameter. If you don’t schedule the connection in a run loop or an operation queue before calling this method, the connection is scheduled in the current run loop in the default mode.

## See Also

### Loading Data Asynchronously
- [init?(request: URLRequest, delegate: Any?)](./init%28request,delegate%29.md)
  Returns an initialized URL connection and begins to load the data for the URL request.
- [init?(request: URLRequest, delegate: Any?, startImmediately: Bool)](./init%28request,delegate,startimmediately%29.md)
  Returns an initialized URL connection and begins to load the data for the URL request, if specified.
- [class func sendAsynchronousRequest(URLRequest, queue: OperationQueue, completionHandler: (URLResponse?, Data?, (any Error)?) -> Void)](./sendasynchronousrequest%28_,queue,completionhandler%29.md)
  Loads the data for a URL request and executes a handler block on an operation queue when the request completes or fails.
- [+ connectionWithRequest:delegate:](./connectionwithrequest_delegate_.md)
  Creates and returns an initialized URL connection and begins to load the data for the URL request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnection/start())*