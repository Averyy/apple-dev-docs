# FoveatedStreamingProviderEndpoint

**Framework**: Foveated Streaming  
**Kind**: enum

The streaming endpoint provided to a [`FoveatedStreamingProvider`](foveatedstreamingprovider.md) extension.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum FoveatedStreamingProviderEndpoint
```

## Topics

### Structures
- [FoveatedStreamingProviderEndpoint.LocalPairingInformation](foveatedstreamingproviderendpoint/localpairinginformation.md)
  Information obtained during QR code pairing for a local connection.
### Enumeration Cases
- [case local(ipAddress: any IPAddress, pairingInformation: FoveatedStreamingProviderEndpoint.LocalPairingInformation)](foveatedstreamingproviderendpoint/local(ipaddress:pairinginformation:).md)
  A local streaming endpoint on the same network.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func streamingProviderScene<Provider>(providerType: Provider.Type) -> some AppExtensionScene](streamingproviderscene(providertype:).md)
  Creates a complete app extension scene for a foveated streaming provider extension.
- [protocol FoveatedStreamingProvider](foveatedstreamingprovider.md)
  Protocol that streaming provider system extensions must implement.
- [protocol FoveatedStreamingProviderContext](foveatedstreamingprovidercontext.md)
- [struct FocusRegion](focusregion.md)
  Eye input data that describes where the end user is looking, relative to the device pose.
- [enum StreamingProviderStatus](streamingproviderstatus.md)
  An enum describing the state of a [`FoveatedStreamingProvider`](foveatedstreamingprovider.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingproviderendpoint)*