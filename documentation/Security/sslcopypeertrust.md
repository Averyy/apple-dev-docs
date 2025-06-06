# SSLCopyPeerTrust(_:_:)

**Framework**: Security  
**Kind**: func

Retrieves a trust management object for the certificate used by a session.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+

## Declaration

```swift
func SSLCopyPeerTrust(_ context: SSLContext, _ trust: UnsafeMutablePointer<SecTrust?>) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

This function is valid any time after a handshake attempt.

## Parameters

- `context`: An SSL session context reference.
- `trust`: On return, a trust management object you can use to evaluate trust for the certificate used by the session. A trust management object includes the certificate to be verified plus the policy or policies to be used in evaluating trust. See   for functions to create and evaluate trust management objects. You must call the   function for this object when you are finished with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslcopypeertrust(_:_:))*