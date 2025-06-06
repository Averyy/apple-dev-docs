# SSLSetProtocolVersionMax(_:_:)

**Framework**: Security  
**Kind**: func

Sets the maximum protocol version allowed by the application for a given SSL context.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
func SSLSetProtocolVersionMax(_ context: SSLContext, _ maxVersion: SSLProtocol) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

## Parameters

- `context`: The SSL context associated with the connection.
- `maxVersion`: The new maximum version ( , for example). See   for a complete list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetprotocolversionmax(_:_:))*