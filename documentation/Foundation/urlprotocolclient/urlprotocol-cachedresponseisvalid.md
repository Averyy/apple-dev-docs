# urlProtocol(_:cachedResponseIsValid:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Tells the client that a cached response is valid.

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
func urlProtocol(_ protocol: URLProtocol, cachedResponseIsValid cachedResponse: CachedURLResponse)
```

## Parameters

- `protocol`: The URL protocol object sending the message.
- `cachedResponse`: The cached response whose validity is being communicated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocolclient/urlprotocol(_:cachedresponseisvalid:))*