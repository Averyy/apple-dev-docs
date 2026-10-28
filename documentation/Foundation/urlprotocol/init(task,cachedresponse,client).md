# init(task:cachedResponse:client:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a URL protocol instance to handle the task.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(task: URLSessionTask, cachedResponse: CachedURLResponse?, client: (any URLProtocolClient)?)
```

```objc
- (instancetype) initWithTask:(NSURLSessionTask *) task cachedResponse:(NSCachedURLResponse *) cachedResponse client:(id<NSURLProtocolClient>) client;
```

## Return Value

The initialized protocol object.

## Discussion

Subclasses should override this method to do any custom initialization. Don’t call this method explicitly. When you register your custom protocol class, the system will initialize instances of your protocol as needed.

This initializer calls through to [`init(request:cachedResponse:client:)`](./init%28request,cachedresponse,client%29.md).

## Parameters

- `task`: A task containing a URL request to be performed by the protocol.
- `cachedResponse`: A cached response for the task; may be `nil` if there is no existing cached response for the task.
- `client`: An object that provides an implementation of the [`URLProtocolClient`](../urlprotocolclient.md) protocol that this instance uses to communicate with the URL loading system. This client object is retained.

## See Also

### Creating protocol objects
- [init(request: URLRequest, cachedResponse: CachedURLResponse?, client: (any URLProtocolClient)?)](./init%28request,cachedresponse,client%29.md)
  Creates a URL protocol instance to handle the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocol/init(task:cachedresponse:client:))*