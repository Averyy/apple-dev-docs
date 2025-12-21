# start()

**Framework**: Foundation  
**Kind**: method

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

#### Discussion

Calling this method is necessary only if you create a connection with the [`init(request:delegate:startImmediately:)`](nsurlconnection/init(request:delegate:startimmediately:).md) method and provide [`false`](https://developer.apple.com/documentation/Swift/false) for the `startImmediately` parameter. If you don’t schedule the connection in a run loop or an operation queue before calling this method, the connection is scheduled in the current run loop in the default mode.

## See Also

- [init?(request: URLRequest, delegate: Any?)](nsurlconnection/init(request:delegate:).md)
  Returns an initialized URL connection and begins to load the data for the URL request.
- [init?(request: URLRequest, delegate: Any?, startImmediately: Bool)](nsurlconnection/init(request:delegate:startimmediately:).md)
  Returns an initialized URL connection and begins to load the data for the URL request, if specified.
- [class func sendAsynchronousRequest(URLRequest, queue: OperationQueue, completionHandler: (URLResponse?, Data?, (any Error)?) -> Void)](nsurlconnection/sendasynchronousrequest(_:queue:completionhandler:).md)
  Loads the data for a URL request and executes a handler block on an operation queue when the request completes or fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnection/start())*