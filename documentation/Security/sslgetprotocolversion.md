# SSLGetProtocolVersion

**Framework**: Security  
**Kind**: func  
**Role**: Function

Gets the SSL protocol version.

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

> **Deprecated**: Use [`SSLGetProtocolVersionMin(_:_:)`](./sslgetprotocolversionmin%28_,_%29.md) and/or [`SSLGetProtocolVersionMax(_:_:)`](./sslgetprotocolversionmax%28_,_%29.md) to check whether a protocol is enabled.

## Declaration

```c
OSStatus SSLGetProtocolVersion(SSLContextRef context, SSLProtocol *protocol);
```

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Parameters

- `context`: An SSL session context reference.
- `protocol`: On return, a pointer to the SSL protocol version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetprotocolversion)*