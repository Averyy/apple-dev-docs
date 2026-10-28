# SSLCopyTrustedRoots

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves the current list of trusted root certificates.

**Availability**:
- macOS 10.5+ - Deprecated in 10.9

> **Deprecated**: To get the current set of trusted roots, call the [`SSLCopyPeerTrust(_:_:)`](./sslcopypeertrust%28_,_%29.md) function to obtain the [`SecTrust`](./sectrust.md) for the peer certificate chain, and then call the [`SecTrustCopyCustomAnchorCertificates(_:_:)`](./sectrustcopycustomanchorcertificates%28_,_%29.md) function (see the [Trust](./trust.md) section of [Certificate, Key, and Trust Services](./certificate-key-and-trust-services.md)).

## Declaration

```c
OSStatus SSLCopyTrustedRoots(SSLContextRef context, CFArrayRef*trustedRoots);
```

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Discussion

You can use the [`SSLSetTrustedRoots`](./sslsettrustedroots.md) function to replace or add to the set of trusted root certificates. If [`SSLSetTrustedRoots`](./sslsettrustedroots.md) has never been called for this session, the [`SSLCopyTrustedRoots`](./sslcopytrustedroots.md) function returns the system’s default set of trusted root certificates.

## Parameters

- `context`: An SSL session context reference.
- `trustedRoots`: On return, a pointer to a value of type `CFArrayRef`. This array contains values of type `SecCertificateRef` representing the current set of trusted roots. You must call the `CFRelease` function to release this array when you are finished with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslcopytrustedroots)*