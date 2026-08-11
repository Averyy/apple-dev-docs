# FoveatedStreamingProviderEndpoint.LocalPairingInformation

**Framework**: Foveated Streaming  
**Kind**: struct

Information obtained during QR code pairing for a local connection.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct LocalPairingInformation
```

## Topics

### Instance Properties
- [let barcodeData: Data](foveatedstreamingproviderendpoint/localpairinginformation/barcodedata.md)
  The raw barcode data as read from the scanned QR code.
- [let barcodeString: String?](foveatedstreamingproviderendpoint/localpairinginformation/barcodestring.md)
  The barcode content decoded as a UTF-8 string, if representable.
- [let expectedCertificateFingerprint: Data?](foveatedstreamingproviderendpoint/localpairinginformation/expectedcertificatefingerprint.md)
  The SHA-256 fingerprint of the server’s TLS certificate, as attested by the session management protocol during a previous successful pairing.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingproviderendpoint/localpairinginformation)*