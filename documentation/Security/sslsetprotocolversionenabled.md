# SSLSetProtocolVersionEnabled

**Framework**: Security  
**Kind**: func  
**Role**: Function

Sets the allowed Secure Sockets Layer (SSL) protocol versions.

**Availability**:
- macOS 10.2+ - Deprecated in 10.9

> **Deprecated**: Use [`SSLSetProtocolVersionMin(_:_:)`](./sslsetprotocolversionmin%28_,_%29.md) and/or [`SSLSetProtocolVersionMax(_:_:)`](./sslsetprotocolversionmax%28_,_%29.md) to specify which protocols are enabled.

## Declaration

```c
OSStatus SSLSetProtocolVersionEnabled(SSLContextRef context, SSLProtocol protocol, Boolean enable);
```

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

#### Discussion

Calling this function is optional. The default is that all supported protocols are enabled. When you call this function, only the specified protocol is affected. Therefore, if you call it once to disable SSL version 2 (for example), the other protocols all remain enabled. You may call this function as many times as you wish to enable and disable specific protocols. You can specify one of the following values for the `protocol` parameter:

- `kSSLProtocol2`
- `kSSLProtocol3`
- `kTLSProtocol1`
- `kSSLProtocolAll`

This function cannot be called when a session is active.

## Parameters

- `context`: An SSL session context reference.
- `protocol`: The SSL protocol version to enable. Pass `kSSLProtocolAll` to enable all protocols.
- `enable`: A Boolean value indicating whether to enable or disable the specified protocol. Specify `true` to enable the protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetprotocolversionenabled)*