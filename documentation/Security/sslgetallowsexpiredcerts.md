# SSLGetAllowsExpiredCerts

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves the value specifying whether expired certificates are allowed.

**Availability**:
- macOS 10.2+ - Deprecated in 10.9

> **Deprecated**: See the replacement procedure for allowing expired certificates in the deprecation summary of [`SSLSetAllowsExpiredCerts`](./sslsetallowsexpiredcerts.md).

## Declaration

```c
OSStatus SSLGetAllowsExpiredCerts(SSLContextRef context, Boolean *allowsExpired);
```

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Discussion

You can set the `allowsExpired` flag to allow the handshake to succeed even if one or more certificates in the certificate chain have expired. This function returns the current setting of this flag. Use the [`SSLSetAllowsExpiredCerts`](./sslsetallowsexpiredcerts.md) function to set the value of the `allowsExpired` flag.

## Parameters

- `context`: An SSL session context reference.
- `allowsExpired`: On return, this flag is set to the value of the Boolean flag that specifies whether expired certificates are ignored. If this value is `true`, then Secure Transport does not return an error if any certificates in the certificate chain are expired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetallowsexpiredcerts)*