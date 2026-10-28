# cachedResponse

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The protocol’s cached response.

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
@NSCopying
var cachedResponse: CachedURLResponse? { get }
```

```objc
@property (copy, readonly, nullable) NSCachedURLResponse * cachedResponse;
```

## Discussion

If not overridden in a subclass, this method returns the cached response stored at initialization time.

## See Also

### Getting protocol attributes
- [var client: (any URLProtocolClient)?](./client.md)
  The object the protocol uses to communicate with the URL loading system.
- [protocol URLProtocolClient](../urlprotocolclient.md)
  The interface used by [`URLProtocol`](../urlprotocol.md) subclasses to communicate with the URL Loading System.
- [var request: URLRequest](./request.md)
  The protocol’s request.
- [var task: URLSessionTask?](./task.md)
  The protocol’s task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocol/cachedresponse)*