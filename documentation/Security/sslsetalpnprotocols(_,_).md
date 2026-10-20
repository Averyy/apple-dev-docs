# SSLSetALPNProtocols(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Sets the list of supported applicaiton layer protocols.

**Availability**:
- iOS 11.0+ - Deprecated in 13.0
- iPadOS 11.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.13+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLSetALPNProtocols(_ context: SSLContext, _ protocols: CFArray) -> OSStatus
```

```c
OSStatus SSLSetALPNProtocols(SSLContextRef context, CFArrayRef protocols);
```

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Parameters

- `context`: The session context.
- `protocols`: An array of ASCII-encoded strings representing the supported protocols, such as `http/1.1`. See [RFC 7301](https://tools.ietf.org/html/rfc7301) for more details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetalpnprotocols(_:_:))*