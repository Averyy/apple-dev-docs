# FoveatedStreamingProviderEndpoint

**Framework**: Foveated Streaming  
**Kind**: enum  
**Role**: Enumeration

The streaming endpoint provided to a `FoveatedStreamingProvider` extension.

**Availability**:
- visionOS 27.0+

## Declaration

```swift
enum FoveatedStreamingProviderEndpoint
```

## Topics

### Structures
- [FoveatedStreamingProviderEndpoint.Local](./foveatedstreamingproviderendpoint/local.md)
  Information needed to connect to a local streaming endpoint.
- [FoveatedStreamingProviderEndpoint.LocalPairingInformation](./foveatedstreamingproviderendpoint/localpairinginformation.md)
  Information obtained during QR code pairing for a local connection.
- [FoveatedStreamingProviderEndpoint.Remote](./foveatedstreamingproviderendpoint/remote.md)
  Information needed to connect to a remote (cloud) streaming endpoint.
### Enumeration Cases
- [case local(FoveatedStreamingProviderEndpoint.Local)](./foveatedstreamingproviderendpoint/local%28_%29.md)
  A local streaming endpoint on the same network.
- [case remote(FoveatedStreamingProviderEndpoint.Remote)](./foveatedstreamingproviderendpoint/remote%28_%29.md)
  A remote (cloud) streaming endpoint.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Streaming provider extensions
- [class FoveatedStreamingProviderContext](./foveatedstreamingprovidercontext.md)
  Context object provided to a streaming provider when it connects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingproviderendpoint)*