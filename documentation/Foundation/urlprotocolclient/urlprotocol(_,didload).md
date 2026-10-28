# urlProtocol(_:didLoad:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) URLProtocol:(NSURLProtocol *) protocol didLoadData:(NSData *) data;
```

## Discussion

The data object must contain only new data loaded since the previous invocation of this method.

## Parameters

- `protocol`: The URL protocol object sending the message.
- `data`: The data being made available.

## See Also

### Indicating loading progress or failure
- [func urlProtocol(URLProtocol, didFailWithError: any Error)](./urlprotocol%28_,didfailwitherror%29.md)
  Tells the client that the load request failed due to an error.
- [func urlProtocolDidFinishLoading(URLProtocol)](./urlprotocoldidfinishloading%28_%29.md)
  Tells the client that the protocol implementation has finished loading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocolclient/urlprotocol(_:didload:))*