# SSLCopyPeerCertificates

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves a peer certificate and its certificate chain.

**Availability**:
- macOS 10.5+ - Deprecated in 10.9

> **Deprecated**: To get peer certificates, call [`SSLCopyPeerTrust(_:_:)`](./sslcopypeertrust%28_,_%29.md) to obtain the [`SecTrust`](./sectrust.md) for the peer certificate chain, then use the [`SecTrustGetCertificateCount(_:)`](./sectrustgetcertificatecount%28_%29.md) and [`SecTrustGetCertificateAtIndex(_:_:)`](./sectrustgetcertificateatindex%28_,_%29.md) functions to retrieve individual certificates in the chain (see the [Trust](./trust.md) section of [Certificate, Key, and Trust Services](./certificate-key-and-trust-services.md)).

## Declaration

```c
OSStatus SSLCopyPeerCertificates(SSLContextRef context, CFArrayRef*certs);
```

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Discussion

This function is valid any time after a handshake attempt. You can use it to examine a peer certificate, to examine a certificate chain to determine why a handshake attempt failed, or to retrieve the certificate chain in order to validate the certificate yourself. (To disable validation so that you can validate the certificate yourself, use the [`SSLSetSessionOption(_:_:_:)`](./sslsetsessionoption%28_,_,_%29.md) function to set the session’s [`SSLSessionOption.breakOnServerAuth`](./sslsessionoption/breakonserverauth.md) flag.)

## Parameters

- `context`: An SSL session context reference.
- `certs`: On return, a pointer to an array of values of type `SecCertificateRef` representing the peer certificate and the certificate chain used to validate it. The certificate at index 0 of the returned array is the peer certificate (the subject of the function call—the end certificate in the chain); the root certificate (or the closest certificate to it) is at the end of the returned array. The entire array is created by the Secure Transport library; you must call the `CFRelease` function for this array when you are finished with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslcopypeercertificates)*