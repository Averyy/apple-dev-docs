# SSLSetAllowsExpiredCerts

**Framework**: Security  
**Kind**: func  
**Role**: Function

Specifies whether certificate expiration times are ignored.

**Availability**:
- macOS 10.2+ - Deprecated in 10.9

> **Deprecated**: To ignore expired certificate errors, first disable Secure Transport’s automatic verification of peer certificates by calling [`SSLSetSessionOption(_:_:_:)`](./sslsetsessionoption%28_,_,_%29.md) to set [`SSLSessionOption.breakOnServerAuth`](./sslsessionoption/breakonserverauth.md) to true. When [`SSLHandshake(_:)`](./sslhandshake%28_%29.md) subsequently returns an `errSSLServerAuthCompleted` result, obtain the [`SecTrust`](./sectrust.md) for the peer’s certificates and perform a custom trust evaluation with [`SecTrust`](./sectrust.md) APIs (see the [Trust](./trust.md) section of [Certificate, Key, and Trust Services](./certificate-key-and-trust-services.md)). The [`SecTrustSetOptions(_:_:)`](./sectrustsetoptions%28_,_%29.md) function allows you to specify that the expiration status of certificates should be ignored for this evaluation.

## Declaration

```c
OSStatus SSLSetAllowsExpiredCerts(SSLContextRef context, Boolean allowsExpired);
```

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Discussion

You can use this function to allow the handshake to succeed even if one or more certificates in the certificate chain have expired. You can use the [`SSLGetAllowsExpiredCerts`](./sslgetallowsexpiredcerts.md) function to determine the current setting of the `allowsExpired` flag.

Use the [`SSLSetAllowsExpiredRoots`](./sslsetallowsexpiredroots.md) function to set a flag specifying whether expired root certificates are allowed.

## Parameters

- `context`: An SSL session context reference.
- `allowsExpired`: A Boolean flag representing whether the certificate expiration times are ignored. The default for this flag is `false`, meaning expired certificates result in an `errSSLCertExpired` result code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetallowsexpiredcerts)*