# sendAsynchronousRequest(_:queue:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Loads the data for a URL request and executes a handler block on an operation queue when the request completes or fails.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func sendAsynchronousRequest(_ request: URLRequest, queue: OperationQueue) async throws -> (URLResponse, Data)
```

#### Discussion

If the request completes successfully, the `data` parameter of the handler block contains the resource data, and the `error` parameter is `nil`.  If the request fails, the `data` parameter is `nil` and the error parameter contain information about the failure.

If authentication is required in order to download the request, the required credentials must be specified as part of the URL. If authentication fails, or credentials are missing, the connection will attempt to continue without credentials. If the request finishes with a `401 Unauthorized` status code, the `response` parameter is `nil`, the `data` parameter contains the resource data, and the `error` parameter is an `NSError` with the [`NSURLErrorUserCancelledAuthentication`](nsurlerrorusercancelledauthentication-swift.var.md) code in the [`NSURLErrorDomain`](nsurlerrordomain.md) error domain.

## Parameters

- `request`: The URL request to load. The   object is deep-copied as part of the initialization process. Changes made to   after this method returns do not affect the request that is used for the loading process.
- `queue`: The operation queue to which the handler block is dispatched when the request completes or failed.
- `handler`: The handler block to execute.

## See Also

- [init?(request: URLRequest, delegate: Any?)](nsurlconnection/init(request:delegate:).md)
  Returns an initialized URL connection and begins to load the data for the URL request.
- [init?(request: URLRequest, delegate: Any?, startImmediately: Bool)](nsurlconnection/init(request:delegate:startimmediately:).md)
  Returns an initialized URL connection and begins to load the data for the URL request, if specified.
- [func start()](nsurlconnection/start.md)
  Causes the connection to begin loading data, if it has not already.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnection/sendasynchronousrequest(_:queue:completionhandler:))*