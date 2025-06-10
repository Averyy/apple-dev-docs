# request

**Framework**: Foundation  
**Kind**: property

The protocol’s request.

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
var request: URLRequest { get }
```

## See Also

- [var cachedResponse: CachedURLResponse?](urlprotocol/cachedresponse.md)
  The protocol’s cached response.
- [var client: (any URLProtocolClient)?](urlprotocol/client.md)
  The object the protocol uses to communicate with the URL loading system.
- [protocol URLProtocolClient](urlprotocolclient.md)
  The interface used by [`URLProtocol`](urlprotocol.md) subclasses to communicate with the URL Loading System.
- [var task: URLSessionTask?](urlprotocol/task.md)
  The protocol’s task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocol/request)*