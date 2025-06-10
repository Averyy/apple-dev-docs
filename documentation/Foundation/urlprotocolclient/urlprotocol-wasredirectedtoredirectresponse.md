# urlProtocol(_:wasRedirectedTo:redirectResponse:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Tells the client that the protocol implementation has been redirected.

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
func urlProtocol(_ protocol: URLProtocol, wasRedirectedTo request: URLRequest, redirectResponse: URLResponse)
```

## Parameters

- `protocol`: The URL protocol object sending the message.
- `request`: The new request that the original request was redirected to.
- `redirectResponse`: The response from the original request that caused the redirect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocolclient/urlprotocol(_:wasredirectedto:redirectresponse:))*