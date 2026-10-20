# SSLGetClientCertificateState(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves the exchange status of the client certificate.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.3+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLGetClientCertificateState(_ context: SSLContext, _ clientState: UnsafeMutablePointer<SSLClientCertificateState>) -> OSStatus
```

```c
OSStatus SSLGetClientCertificateState(SSLContextRef context, SSLClientCertificateState *clientState);
```

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

#### Discussion

The value returned reflects the latest change in the state of the client certificate exchange. If either peer initiates a renegotiation attempt, Secure Transport resets the state to `kSSLClientCertNone`.

## Parameters

- `context`: An SSL session context reference.
- `clientState`: On return, a pointer to a value indicating the state of the client certificate exchange. See [`SSLClientCertificateState`](./sslclientcertificatestate.md) for a list of possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetclientcertificatestate(_:_:))*