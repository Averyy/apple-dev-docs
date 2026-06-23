# FoveatedStreamingProvider.Endpoint.local(ipAddress:pairingInformation:)

**Framework**: Foveated Streaming  
**Kind**: case

A local streaming endpoint on the same network.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
case local(ipAddress: any IPAddress, pairingInformation: FoveatedStreamingProvider.Endpoint.LocalPairingInformation)
```

## Parameters

- `ipAddress`: The IP address of the streaming PC.
- `barcode`: Opaque credential data obtained during QR code pairing. The extension is responsible for decoding this (e.g., extracting client tokens for CloudXR).
- `expectedCertificateFingerprint`: The SHA-256 fingerprint of the server’s TLS certificate, as attested by the session management protocol during a previous successful pairing. The extension **must** verify the server’s actual certificate matches this value. `nil` for first-time connections where no stored credentials exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovider/endpoint/local(ipaddress:pairinginformation:))*