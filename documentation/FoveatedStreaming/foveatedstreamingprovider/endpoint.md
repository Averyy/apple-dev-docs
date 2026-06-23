# FoveatedStreamingProvider.Endpoint

**Framework**: Foveated Streaming  
**Kind**: enum

The streaming endpoint provided to a [`FoveatedStreamingProvider`](foveatedstreamingprovider.md) extension.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum Endpoint
```

#### Overview

This describes where the extension should connect to stream content.

## Topics

### Structures
- [FoveatedStreamingProvider.Endpoint.LocalPairingInformation](foveatedstreamingprovider/endpoint/localpairinginformation.md)
  Information obtained during QR code pairing for a local connection.
### Enumeration Cases
- [case local(ipAddress: any IPAddress, pairingInformation: FoveatedStreamingProvider.Endpoint.LocalPairingInformation)](foveatedstreamingprovider/endpoint/local(ipaddress:pairinginformation:).md)
  A local streaming endpoint on the same network.
- [FoveatedStreamingProvider.Endpoint.remote(url:signalingHeaders:)](foveatedstreamingprovider/endpoint/remote(url:signalingheaders:).md)
  A remote (cloud) streaming endpoint.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovider/endpoint)*