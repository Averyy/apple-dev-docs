# SSLSetEnableCertVerify

**Framework**: Security  
**Kind**: func  
**Role**: Function

Enables or disables peer certificate chain validation.

**Availability**:
- macOS 10.2+ - Deprecated in 10.9

> **Deprecated**: To disable peer certificate chain validation, you can instead use [`SSLSetSessionOption(_:_:_:)`](./sslsetsessionoption%28_,_,_%29.md) to set [`SSLSessionOption.breakOnServerAuth`](./sslsessionoption/breakonserverauth.md) to true. This will disable verification and cause [`SSLHandshake(_:)`](./sslhandshake%28_%29.md) to return with an `errSSLServerAuthCompleted` result when the peer certificates have been received. Then you can choose to evaluate peer trust yourself or simply call [`SSLHandshake(_:)`](./sslhandshake%28_%29.md) again to proceed with the handshake.

## Declaration

```c
OSStatus SSLSetEnableCertVerify(SSLContextRef context, Boolean enableVerify);
```

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

#### Discussion

By default, Secure Transport attempts to verify the certificate chain during an exchange of peer certificates. If you disable peer certificate chain validation, it is your responsibility to call [`SSLCopyPeerCertificates`](./sslcopypeercertificates.md) upon successful completion of the handshake and then to validate the peer certificate chain before transferring the data.

You can use the [`SSLGetEnableCertVerify`](./sslgetenablecertverify.md) function to determine the current setting of the `enableVerify` flag.

## Parameters

- `context`: An SSL session context reference.
- `enableVerify`: A Boolean value specifying whether peer certificate chain validation is enabled. Certificate chain validation is enabled by default. Specify `false` to disable validation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetenablecertverify)*