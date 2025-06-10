# task

**Framework**: Foundation  
**Kind**: property

The protocol’s task.

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
@NSCopying
var task: URLSessionTask? { get }
```

## See Also

- [var cachedResponse: CachedURLResponse?](urlprotocol/cachedresponse.md)
  The protocol’s cached response.
- [var client: (any URLProtocolClient)?](urlprotocol/client.md)
  The object the protocol uses to communicate with the URL loading system.
- [protocol URLProtocolClient](urlprotocolclient.md)
  The interface used by [`URLProtocol`](urlprotocol.md) subclasses to communicate with the URL Loading System.
- [var request: URLRequest](urlprotocol/request.md)
  The protocol’s request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocol/task)*