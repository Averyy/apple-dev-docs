# SSLCopyPeerTrust(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves a trust management object for the certificate used by a session.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.6+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLCopyPeerTrust(_ context: SSLContext, _ trust: UnsafeMutablePointer<SecTrust?>) -> OSStatus
```

```c
OSStatus SSLCopyPeerTrust(SSLContextRef context, SecTrustRef*trust);
```

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Discussion

This function is valid any time after a handshake attempt.

## Parameters

- `context`: An SSL session context reference.
- `trust`: On return, a trust management object you can use to evaluate trust for the certificate used by the session. A trust management object includes the certificate to be verified plus the policy or policies to be used in evaluating trust. See [Certificate, Key, and Trust Services](./certificate-key-and-trust-services.md) for functions to create and evaluate trust management objects. You must call the `CFRelease` function for this object when you are finished with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslcopypeertrust(_:_:))*