# init(request:delegate:startImmediately:)

**Framework**: Foundation  
**Kind**: init

Returns an initialized URL connection and begins to load the data for the URL request, if specified.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init?(request: URLRequest, delegate: Any?, startImmediately: Bool)
```

#### Return Value

The URL connection for the URL request. Returns `nil` if a connection can’t be initialized.

#### Discussion

During the download the connection maintains a strong reference to the `delegate`. It releases that strong reference when the connection finishes loading, fails, or is canceled.

## Parameters

- `request`: The URL request to load. The   object is deep-copied as part of the initialization process. Changes made to   after this method returns do not affect the request that is used for the loading process.
- `delegate`: The delegate object for the connection. The connection calls methods on this delegate as the load progresses.
- `startImmediately`:   if the connection should begin loading data immediately, otherwise  . If you pass  , the connection is not scheduled with a run loop. You can then schedule the connection in the run loop and mode of your choice by calling  .

## See Also

- [init?(request: URLRequest, delegate: Any?)](nsurlconnection/init(request:delegate:).md)
  Returns an initialized URL connection and begins to load the data for the URL request.
- [class func sendAsynchronousRequest(URLRequest, queue: OperationQueue, completionHandler: (URLResponse?, Data?, (any Error)?) -> Void)](nsurlconnection/sendasynchronousrequest(_:queue:completionhandler:).md)
  Loads the data for a URL request and executes a handler block on an operation queue when the request completes or fails.
- [func start()](nsurlconnection/start.md)
  Causes the connection to begin loading data, if it has not already.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnection/init(request:delegate:startimmediately:))*