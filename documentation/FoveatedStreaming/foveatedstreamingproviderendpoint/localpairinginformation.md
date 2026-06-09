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

### Initializers
- [init(barcodeData: Data, barcodeString: String?, expectedCertificateFingerprint: Data?)](foveatedstreamingproviderendpoint/localpairinginformation/init(barcodedata:barcodestring:expectedcertificatefingerprint:).md)
### Instance Properties
- [var barcodeData: Data](foveatedstreamingproviderendpoint/localpairinginformation/barcodedata.md)
  The raw barcode data as read from the scanned QR code.
- [var barcodeString: String?](foveatedstreamingproviderendpoint/localpairinginformation/barcodestring.md)
  The barcode content decoded as a UTF-8 string, if representable.
- [var expectedCertificateFingerprint: Data?](foveatedstreamingproviderendpoint/localpairinginformation/expectedcertificatefingerprint.md)
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