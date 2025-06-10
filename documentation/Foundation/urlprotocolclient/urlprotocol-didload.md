# urlProtocol(_:didLoad:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Tells the client that the protocol implementation has loaded some data.

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
func urlProtocol(_ protocol: URLProtocol, didLoad data: Data)
```

#### Discussion

The data object must contain only new data loaded since the previous invocation of this method.

## Parameters

- `protocol`: The URL protocol object sending the message.
- `data`: The data being made available.

## See Also

- [func urlProtocol(URLProtocol, didFailWithError: any Error)](urlprotocolclient/urlprotocol(_:didfailwitherror:).md)
  Tells the client that the load request failed due to an error.
- [func urlProtocolDidFinishLoading(URLProtocol)](urlprotocolclient/urlprotocoldidfinishloading(_:).md)
  Tells the client that the protocol implementation has finished loading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocolclient/urlprotocol(_:didload:))*