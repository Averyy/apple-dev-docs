# SSLSetProtocolVersionMin(_:_:)

**Framework**: Security  
**Kind**: func

Sets the minimum protocol version allowed by the application for a given SSL context.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
func SSLSetProtocolVersionMin(_ context: SSLContext, _ minVersion: SSLProtocol) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

## Parameters

- `context`: The SSL context associated with the connection.
- `minVersion`: The new minimum version ( , for example). See   for a complete list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetprotocolversionmin(_:_:))*