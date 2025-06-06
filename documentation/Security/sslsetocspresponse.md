# SSLSetOCSPResponse(_:_:)

**Framework**: Security  
**Kind**: func

Sets the OCSP response for the given SSL session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+

## Declaration

```swift
func SSLSetOCSPResponse(_ context: SSLContext, _ response: CFData) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

## Parameters

- `context`: A session context.
- `response`: A non-    instance containing the bytes of the OCSP response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetocspresponse(_:_:))*