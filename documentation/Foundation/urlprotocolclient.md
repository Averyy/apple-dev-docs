# URLProtocolClient

**Framework**: Foundation  
**Kind**: protocol

The interface used by [`URLProtocol`](urlprotocol.md) subclasses to communicate with the URL Loading System.

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
protocol URLProtocolClient : NSObjectProtocol, Sendable
```

#### Overview

Don’t implement this protocol in your application. Instead, your [`URLProtocol`](urlprotocol.md) subclass calls methods of this protocol on its own [`client`](urlprotocol/client.md) property.

## Topics

### Creating a response
- [func urlProtocol(URLProtocol, didReceive: URLResponse, cacheStoragePolicy: URLCache.StoragePolicy)](urlprotocolclient/urlprotocol(_:didreceive:cachestoragepolicy:).md)
  Tells the client that the protocol implementation has created a response object for the request.
### Handling redirects
- [func urlProtocol(URLProtocol, wasRedirectedTo: URLRequest, redirectResponse: URLResponse)](urlprotocolclient/urlprotocol(_:wasredirectedto:redirectresponse:).md)
  Tells the client that the protocol implementation has been redirected.
### Working with cache data
- [func urlProtocol(URLProtocol, cachedResponseIsValid: CachedURLResponse)](urlprotocolclient/urlprotocol(_:cachedresponseisvalid:).md)
  Tells the client that a cached response is valid.
### Handling authentication challenges
- [func urlProtocol(URLProtocol, didCancel: URLAuthenticationChallenge)](urlprotocolclient/urlprotocol(_:didcancel:).md)
  Tells the client that an authentication challenge has been canceled.
- [func urlProtocol(URLProtocol, didReceive: URLAuthenticationChallenge)](urlprotocolclient/urlprotocol(_:didreceive:).md)
  Tells the client that the URL Loading System received an authentication challenge.
### Indicating loading progress or failure
- [func urlProtocol(URLProtocol, didFailWithError: any Error)](urlprotocolclient/urlprotocol(_:didfailwitherror:).md)
  Tells the client that the load request failed due to an error.
- [func urlProtocol(URLProtocol, didLoad: Data)](urlprotocolclient/urlprotocol(_:didload:).md)
  Tells the client that the protocol implementation has loaded some data.
- [func urlProtocolDidFinishLoading(URLProtocol)](urlprotocolclient/urlprotocoldidfinishloading(_:).md)
  Tells the client that the protocol implementation has finished loading.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var cachedResponse: CachedURLResponse?](urlprotocol/cachedresponse.md)
  The protocol’s cached response.
- [var client: (any URLProtocolClient)?](urlprotocol/client.md)
  The object the protocol uses to communicate with the URL loading system.
- [var request: URLRequest](urlprotocol/request.md)
  The protocol’s request.
- [var task: URLSessionTask?](urlprotocol/task.md)
  The protocol’s task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocolclient)*