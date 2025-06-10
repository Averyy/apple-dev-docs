# urlProtocolDidFinishLoading(_:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Tells the client that the protocol implementation has finished loading.

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
func urlProtocolDidFinishLoading(_ protocol: URLProtocol)
```

## Parameters

- `protocol`: The URL protocol object sending the message.

## See Also

- [func urlProtocol(URLProtocol, didFailWithError: any Error)](urlprotocolclient/urlprotocol(_:didfailwitherror:).md)
  Tells the client that the load request failed due to an error.
- [func urlProtocol(URLProtocol, didLoad: Data)](urlprotocolclient/urlprotocol(_:didload:).md)
  Tells the client that the protocol implementation has loaded some data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocolclient/urlprotocoldidfinishloading(_:))*