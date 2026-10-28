# SSLSetAllowsAnyRoot

**Framework**: Security  
**Kind**: func  
**Role**: Function

Specifies whether root certificates from unrecognized certification authorities are allowed.

**Availability**:
- macOS 10.2+ - Deprecated in 10.9

> **Deprecated**: To ignore unknown root certificate errors, first disable Secure Transport’s automatic verification of peer certificates by calling [`SSLSetSessionOption(_:_:_:)`](./sslsetsessionoption%28_,_,_%29.md) to set [`SSLSessionOption.breakOnServerAuth`](./sslsessionoption/breakonserverauth.md) to [`true`](../Swift/true.md). When [`SSLHandshake(_:)`](./sslhandshake%28_%29.md) subsequently returns an `errSSLServerAuthCompleted` result, obtain the [`SecTrust`](./sectrust.md) for the peer’s certificates and perform a custom trust evaluation with [`SecTrust`](./sectrust.md) APIs (see the [Trust](./trust.md) section of [Certificate, Key, and Trust Services](./certificate-key-and-trust-services.md)). Note that an unknown root certificate will cause [`SecTrustEvaluate(_:_:)`](./sectrustevaluate%28_,_%29.md) to report [`SecTrustResultType.recoverableTrustFailure`](./sectrustresulttype/recoverabletrustfailure.md) as the trust result.

## Declaration

```c
OSStatus SSLSetAllowsAnyRoot(SSLContextRef context, Boolean anyRoot);
```

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Discussion

The system maintains a set of root certificates signed by known, trusted root CAs. When the `anyRoot` flag is `true`, Secure Transport does not return an error if one of the following two conditions occurs:

- The peer returns a certificate chain with a root certificate, and the chain verifies to that root, but the CA for the root certificate is not one of the known, trusted root CAs. This results in an `errSSLUnknownRootCert` result code when the `anyRoot` flag is `false`.
- The peer returns a certificate chain that does not contain a root certificate, and the server can’t verify the chain to one of the trusted root certificates. This results in an `errSSLNoRootCert` result code when the `anyRoot` flag is `false`.

Both of these error conditions are ignored when the `anyRoot` flag is `true`, allowing connection to a peer for which trust could not be established.

If you use this function to allow an untrusted root to be used for validation of a certificate—for example, after prompting the user for permission to do so—remember to set the `anyRoot` Boolean value back to `false`. If you don’t, any random root certificate can be used for signing a certificate chain. To add a certificate to the list of trusted roots, use the [`SecTrustSetAnchorCertificates(_:_:)`](./sectrustsetanchorcertificates%28_,_%29.md) function.

## Parameters

- `context`: An SSL session context reference.
- `anyRoot`: A Boolean flag specifying whether root certificates from unrecognized certification authorities (CAs) are allowed. The default for this flag is `false`, specifying that roots from unrecognized CAs are not allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetallowsanyroot)*