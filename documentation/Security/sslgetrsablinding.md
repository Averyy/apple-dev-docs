# SSLGetRsaBlinding

**Framework**: Security  
**Kind**: func  
**Role**: Function

Obtains a value indicating whether RSA blinding is enabled.

**Availability**:
- macOS 10.2+ - Deprecated in 10.9

> **Deprecated**: RSA blinding is now enabled unconditionally as it prevents a known way for an attacker to recover the private key and the performance gain of disabling it is negligible.

## Declaration

```c
OSStatus SSLGetRsaBlinding(SSLContextRef context, Boolean *blinding);
```

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

#### Discussion

This function is used only on the server side of a connection.

Call the [`SSLSetRsaBlinding`](./sslsetrsablinding.md) function to enable or disable RSA blinding.

## Parameters

- `context`: An SSL session context reference.
- `blinding`: On return, a pointer to a Boolean value indicating whether RSA blinding is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetrsablinding)*