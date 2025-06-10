# init(task:cachedResponse:client:)

**Framework**: Foundation  
**Kind**: init

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

#### Return Value

The initialized protocol object.

#### Discussion

Subclasses should override this method to do any custom initialization. Don’t call this method explicitly. When you register your custom protocol class, the system will initialize instances of your protocol as needed.

This initializer calls through to [`init(request:cachedResponse:client:)`](urlprotocol/init(request:cachedresponse:client:).md).

## Parameters

- `task`: A task containing a URL request to be performed by the protocol.
- `cachedResponse`: A cached response for the task; may be   if there is no existing cached response for the task.
- `client`: An object that provides an implementation of the   protocol that this instance uses to communicate with the URL loading system. This client object is retained.

## See Also

- [init(request: URLRequest, cachedResponse: CachedURLResponse?, client: (any URLProtocolClient)?)](urlprotocol/init(request:cachedresponse:client:).md)
  Creates a URL protocol instance to handle the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocol/init(task:cachedresponse:client:))*