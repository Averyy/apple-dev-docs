# SSLSetAllowsExpiredRoots

**Framework**: Security  
**Kind**: func  
**Role**: Function

Specifies whether expired root certificates are allowed.

**Availability**:
- macOS 10.2+ - Deprecated in 10.9

> **Deprecated**: To ignore expired certificate errors, first disable Secure Transport’s automatic verification of peer certificates by calling [`SSLSetSessionOption(_:_:_:)`](./sslsetsessionoption%28_,_,_%29.md) to set [`SSLSessionOption.breakOnServerAuth`](./sslsessionoption/breakonserverauth.md) to [`true`](../Swift/true.md). When [`SSLHandshake(_:)`](./sslhandshake%28_%29.md) subsequently returns an `errSSLServerAuthCompleted` result, obtain the [`SecTrust`](./sectrust.md) for the peer’s certificates and perform a custom trust evaluation with [`SecTrust`](./sectrust.md) APIs (see the [Trust](./trust.md) section of [Certificate, Key, and Trust Services](./certificate-key-and-trust-services.md)). The [`SecTrustSetOptions(_:_:)`](./sectrustsetoptions%28_,_%29.md) function allows you to specify that the expiration status of certificates should be ignored for this evaluation. The [`allowExpiredRoot`](./sectrustoptionflags/allowexpiredroot.md) option can be used instead of [`allowExpired`](./sectrustoptionflags/allowexpired.md) to allow expired roots only.

## Declaration

```c
OSStatus SSLSetAllowsExpiredRoots(SSLContextRef context, Boolean allowsExpired);
```

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

#### Discussion

The default value for the `allowsExpired` flag is `false`. When this flag is `false`, Secure Transport returns an `errSSLCertExpired` result code during handshake if the root certificate is expired.

You can use the [`SSLGetAllowsExpiredRoots`](./sslgetallowsexpiredroots.md) function to determine the current setting of the `allowsExpired` flag.

Use the [`SSLSetAllowsExpiredCerts`](./sslsetallowsexpiredcerts.md) function to set a value that determines whether expired non-root certificates are allowed.

## Parameters

- `context`: An SSL session context reference.
- `allowsExpired`: A Boolean value indicating whether to allow expired root certificates. Pass `true` to allow expired roots.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetallowsexpiredroots)*