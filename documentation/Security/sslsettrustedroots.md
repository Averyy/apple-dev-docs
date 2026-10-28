# SSLSetTrustedRoots

**Framework**: Security  
**Kind**: func  
**Role**: Function

Augments or replaces the default set of trusted root certificates for this session.

**Availability**:
- macOS 10.2+ - Deprecated in 10.9

> **Deprecated**: To trust specific roots in a session, first disable Secure Transport’s automatic verification of peer certificates by calling [`SSLSetSessionOption(_:_:_:)`](./sslsetsessionoption%28_,_,_%29.md) to set [`SSLSessionOption.breakOnServerAuth`](./sslsessionoption/breakonserverauth.md) to true. When [`SSLHandshake(_:)`](./sslhandshake%28_%29.md) subsequently returns an errSSLServerAuthCompleted result, obtain the [`SecTrust`](./sectrust.md) for the peer’s certificates and perform a custom trust evaluation with [`SecTrust`](./sectrust.md) APIs (see the [Trust](./trust.md) section of [Certificate, Key, and Trust Services](./certificate-key-and-trust-services.md)). You can call [`SecTrustSetAnchorCertificates(_:_:)`](./sectrustsetanchorcertificates%28_,_%29.md) to augment the system’s trusted root set, or [`SecTrustSetAnchorCertificatesOnly(_:_:)`](./sectrustsetanchorcertificatesonly%28_,_%29.md) to make these the only trusted roots, prior to calling [`SecTrustEvaluate(_:_:)`](./sectrustevaluate%28_,_%29.md).

## Declaration

```c
OSStatus SSLSetTrustedRoots(SSLContextRef context, CFArrayRef trustedRoots, Boolean replaceExisting);
```

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Discussion

Each successive call to this function with the `replaceExisting` parameter set to `false` results in accumulation of additional root certificates. To see the current set of trusted root certificates, call the [`SSLCopyTrustedRoots`](./sslcopytrustedroots.md) function.

## Parameters

- `context`: An SSL session context reference.
- `trustedRoots`: A reference to an array of trusted root certificates of type `SecCertificateRef`.
- `replaceExisting`: A Boolean value indicating whether to replace or append the current trusted root certificate set. If this value is `true`, the specified root certificates become the only roots that are trusted during this session. If this value is `false`, the specified root certificates are added to the current set of trusted root certificates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsettrustedroots)*