# SSLGetProtocolVersionEnabled

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves the enabled status of a given protocol.

**Availability**:
- macOS 10.2+ - Deprecated in 10.9

> **Deprecated**: Use [`SSLGetProtocolVersionMin(_:_:)`](./sslgetprotocolversionmin%28_,_%29.md) and/or [`SSLGetProtocolVersionMax(_:_:)`](./sslgetprotocolversionmax%28_,_%29.md) to check whether a protocol is enabled.

## Declaration

```c
OSStatus SSLGetProtocolVersionEnabled(SSLContextRef context, SSLProtocol protocol, Boolean *enable);
```

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Discussion

You can specify any one of the following values for the `protocol` parameter:

- `kSSLProtocol2`
- `kSSLProtocol3`
- `kTLSProtocol1`
- `kSSLProtocolAll` Specify this value to determine whether all protocols are enabled.

## Parameters

- `context`: An SSL session context reference.
- `protocol`: A value of type `SSLProtocol` representing an SSL protocol version.
- `enable`: On return, points to a Boolean value indicating whether the specified protocol version is enabled. If this value is `true`, the protocol is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetprotocolversionenabled)*