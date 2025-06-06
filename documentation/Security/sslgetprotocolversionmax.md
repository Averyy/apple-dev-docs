# SSLGetProtocolVersionMax(_:_:)

**Framework**: Security  
**Kind**: func

Gets the maximum protocol version allowed by the application for a given SSL context.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
func SSLGetProtocolVersionMax(_ context: SSLContext, _ maxVersion: UnsafeMutablePointer<SSLProtocol>) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

## Parameters

- `context`: The SSL context associated with the connection.
- `maxVersion`: The address of an   integer where the maximum version should be stored. See   for a list of possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetprotocolversionmax(_:_:))*