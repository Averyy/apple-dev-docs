# urlProtocolDidFinishLoading(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) URLProtocolDidFinishLoading:(NSURLProtocol *) protocol;
```

## Parameters

- `protocol`: The URL protocol object sending the message.

## See Also

### Indicating loading progress or failure
- [func urlProtocol(URLProtocol, didFailWithError: any Error)](./urlprotocol%28_,didfailwitherror%29.md)
  Tells the client that the load request failed due to an error.
- [func urlProtocol(URLProtocol, didLoad: Data)](./urlprotocol%28_,didload%29.md)
  Tells the client that the protocol implementation has loaded some data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocolclient/urlprotocoldidfinishloading(_:))*