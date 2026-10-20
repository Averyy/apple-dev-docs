# urlProtocol(_:didCancel:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the client that an authentication challenge has been canceled.

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
func urlProtocol(_ protocol: URLProtocol, didCancel challenge: URLAuthenticationChallenge)
```

```objc
- (void) URLProtocol:(NSURLProtocol *) protocol didCancelAuthenticationChallenge:(NSURLAuthenticationChallenge *) challenge;
```

## Parameters

- `protocol`: The URL protocol object sending the message.
- `challenge`: The authentication challenge that was canceled.

## See Also

### Handling authentication challenges
- [func urlProtocol(URLProtocol, didReceive: URLAuthenticationChallenge)](./urlprotocol%28_,didreceive%29.md)
  Tells the client that the URL Loading System received an authentication challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocolclient/urlprotocol(_:didcancel:))*