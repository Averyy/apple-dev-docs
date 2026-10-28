# SSLGetEnableCertVerify

**Framework**: Security  
**Kind**: func  
**Role**: Function

Determines whether peer certificate chain validation is currently enabled.

**Availability**:
- macOS 10.2+ - Deprecated in 10.9

> **Deprecated**: To check whether peer certificate chain validation is enabled in a context, call [`SSLGetSessionOption(_:_:_:)`](./sslgetsessionoption%28_,_,_%29.md) to obtain the value of the [`SSLSessionOption.breakOnServerAuth`](./sslsessionoption/breakonserverauth.md) session option flag. If the value of this option flag is [`true`](../Swift/true.md), then verification is disabled.

## Declaration

```c
OSStatus SSLGetEnableCertVerify(SSLContextRef context, Boolean *enableVerify);
```

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Discussion

Use the [`SSLSetEnableCertVerify`](./sslsetenablecertverify.md) function to set the value of the `enableVerify` flag.

## Parameters

- `context`: An SSL session context reference.
- `enableVerify`: On return, a pointer to a Boolean value specifying whether peer certificate chain validation is enabled. If this value is `true`, then Secure Transport automatically attempts to verify the certificate chain during exchange of peer certificates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetenablecertverify)*