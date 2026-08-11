# expectedCertificateFingerprint

**Framework**: Foveated Streaming  
**Kind**: property

The SHA-256 fingerprint of the server’s TLS certificate, as attested by the session management protocol during a previous successful pairing.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
let expectedCertificateFingerprint: Data?
```

#### Discussion

The extension **must** verify the server’s actual certificate matches this value, if non-`nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingproviderendpoint/localpairinginformation/expectedcertificatefingerprint)*