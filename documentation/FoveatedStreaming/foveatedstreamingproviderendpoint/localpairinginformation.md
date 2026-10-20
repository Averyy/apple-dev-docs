# FoveatedStreamingProviderEndpoint.LocalPairingInformation

**Framework**: Foveated Streaming  
**Kind**: struct  
**Role**: Structure

Information obtained during QR code pairing for a local connection.

**Availability**:
- visionOS 27.0+

## Declaration

```swift
struct LocalPairingInformation
```

## Topics

### Instance Properties
- [let barcodeData: Data](./localpairinginformation/barcodedata.md)
  The raw barcode data as read from the scanned QR code.
- [let barcodeString: String?](./localpairinginformation/barcodestring.md)
  The barcode content decoded as a UTF-8 string, if representable.
- [let expectedCertificateFingerprint: Data?](./localpairinginformation/expectedcertificatefingerprint.md)
  The SHA-256 fingerprint of the server’s TLS certificate, as attested by the session management protocol during a previous successful pairing.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingproviderendpoint/localpairinginformation)*