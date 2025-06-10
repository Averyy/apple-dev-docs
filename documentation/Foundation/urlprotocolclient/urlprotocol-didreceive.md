# urlProtocol(_:didReceive:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Tells the client that the URL Loading System received an authentication challenge.

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
func urlProtocol(_ protocol: URLProtocol, didReceive challenge: URLAuthenticationChallenge)
```

#### Discussion

The protocol client guarantees that it will answer the request on the same thread that called this method. The client may add a default credential to the challenge it issues to the connection delegate, if `protocol` did not provide one.

## Parameters

- `protocol`: The URL protocol object sending the message.
- `challenge`: The authentication challenge that has been received.

## See Also

- [func urlProtocol(URLProtocol, didCancel: URLAuthenticationChallenge)](urlprotocolclient/urlprotocol(_:didcancel:).md)
  Tells the client that an authentication challenge has been canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocolclient/urlprotocol(_:didreceive:))*