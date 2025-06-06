# SecTrustSetOCSPResponse(_:_:)

**Framework**: Security  
**Kind**: func

Attaches Online Certificate Status Protocol (OSCP) response data to a trust object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func SecTrustSetOCSPResponse(_ trust: SecTrust, _ responseData: CFTypeRef?) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

This function allows the caller to provide OCSPResponse data (which may be obtained during a TLS/SSL handshake, per [`RFC3546`](https://developer.apple.comhttps://tools.ietf.org/html/rfc3546)) as input to a trust evaluation. If this data is available, it can obviate the need to contact an OCSP server for current revocation information.

## Parameters

- `trust`: The trust evaluation object to modify.
- `responseData`: Either a   object containing a single DER-encoded OCSPResponse (per  ), or a   of these.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustsetocspresponse(_:_:))*