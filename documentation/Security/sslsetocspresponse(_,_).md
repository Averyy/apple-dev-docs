# SSLSetOCSPResponse(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Sets the OCSP response for the given SSL session.

**Availability**:
- iOS 11.0+ - Deprecated in 13.0
- iPadOS 11.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.13+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLSetOCSPResponse(_ context: SSLContext, _ response: CFData) -> OSStatus
```

```c
OSStatus SSLSetOCSPResponse(SSLContextRef context, CFDataRef response);
```

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Parameters

- `context`: A session context.
- `response`: A non-`NULL` [`CFData`](../CoreFoundation/cfdata.md) instance containing the bytes of the OCSP response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetocspresponse(_:_:))*