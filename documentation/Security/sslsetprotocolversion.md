# SSLSetProtocolVersion

**Framework**: Security  
**Kind**: func  
**Role**: Function

Sets the SSL protocol version.

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

> **Deprecated**: Use [`SSLSetProtocolVersionMin(_:_:)`](./sslsetprotocolversionmin%28_,_%29.md) and/or [`SSLSetProtocolVersionMax(_:_:)`](./sslsetprotocolversionmax%28_,_%29.md) to specify which protocols are enabled.

## Declaration

```c
OSStatus SSLSetProtocolVersion(SSLContextRef context, SSLProtocol version);
```

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Discussion

This function cannot be called when a session is active.

## Parameters

- `context`: An SSL session context reference.
- `version`: The SSL protocol version to negotiate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetprotocolversion)*