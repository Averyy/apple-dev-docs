# urlProtocol(_:didFailWithError:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the client that the load request failed due to an error.

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
func urlProtocol(_ protocol: URLProtocol, didFailWithError error: any Error)
```

```objc
- (void) URLProtocol:(NSURLProtocol *) protocol didFailWithError:(NSError *) error;
```

## Parameters

- `protocol`: The URL protocol object sending the message.
- `error`: The error that caused the failure of the load request.

## See Also

### Indicating loading progress or failure
- [func urlProtocol(URLProtocol, didLoad: Data)](./urlprotocol%28_,didload%29.md)
  Tells the client that the protocol implementation has loaded some data.
- [func urlProtocolDidFinishLoading(URLProtocol)](./urlprotocoldidfinishloading%28_%29.md)
  Tells the client that the protocol implementation has finished loading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocolclient/urlprotocol(_:didfailwitherror:))*