# SSLGetClientCertificateState(_:_:)

**Framework**: Security  
**Kind**: func

Retrieves the exchange status of the client certificate.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.3+

## Declaration

```swift
func SSLGetClientCertificateState(_ context: SSLContext, _ clientState: UnsafeMutablePointer<SSLClientCertificateState>) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

The value returned reflects the latest change in the state of the client certificate exchange. If either peer initiates a renegotiation attempt, Secure Transport resets the state to `kSSLClientCertNone`.

## Parameters

- `context`: An SSL session context reference.
- `clientState`: On return, a pointer to a value indicating the state of the client certificate exchange. See   for a list of possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetclientcertificatestate(_:_:))*