# SecTrustSetSignedCertificateTimestamps(_:_:)

**Framework**: Security  
**Kind**: func

Attaches signed certificate timestamp data to a trust object.

**Availability**:
- iOS 12.1.1+
- iPadOS 12.1.1+
- Mac Catalyst 13.1+
- macOS 10.14.2+
- tvOS 12.1.1+
- visionOS 1.0+
- watchOS 5.1.1+

## Declaration

```swift
func SecTrustSetSignedCertificateTimestamps(_ trust: SecTrust, _ sctArray: CFArray?) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

Use this function to provide secure certificate timestamps, which might be obtained during a TLS/SSL handshake, as input to a trust evaluation. For more information, see [`RFC 6962`](https://developer.apple.comhttps://tools.ietf.org/html/rfc6962).

## Parameters

- `trust`: The trust object to which the timestamp data should be attached.
- `sctArray`: An array of   instances, each of which contains a signed certificate timestamp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustsetsignedcertificatetimestamps(_:_:))*