# StreamingProviderStatus

**Framework**: Foveated Streaming  
**Kind**: enum

An enum describing the state of a [`FoveatedStreamingProvider`](foveatedstreamingprovider.md).

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum StreamingProviderStatus
```

## Topics

### Enumeration Cases
- [StreamingProviderStatus.connected](streamingproviderstatus/connected.md)
  Connected and streaming.
- [StreamingProviderStatus.connecting](streamingproviderstatus/connecting.md)
  [`init(context:)`](foveatedstreamingprovider/init(context:).md) is in progress.
- [StreamingProviderStatus.disconnected(error:)](streamingproviderstatus/disconnected(error:).md)
  The session has been disconnected for the provided reason.
- [StreamingProviderStatus.disconnecting](streamingproviderstatus/disconnecting.md)
  [`disconnect()`](foveatedstreamingprovider/disconnect().md) has been called.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func streamingProviderScene<Provider>(providerType: Provider.Type) -> some AppExtensionScene](streamingproviderscene(providertype:).md)
  Creates a complete app extension scene for a foveated streaming provider extension.
- [protocol FoveatedStreamingProvider](foveatedstreamingprovider.md)
  Protocol that streaming provider system extensions must implement.
- [protocol FoveatedStreamingProviderContext](foveatedstreamingprovidercontext.md)
- [enum FoveatedStreamingProviderEndpoint](foveatedstreamingproviderendpoint.md)
  The streaming endpoint provided to a [`FoveatedStreamingProvider`](foveatedstreamingprovider.md) extension.
- [struct FocusRegion](focusregion.md)
  Eye input data that describes where the end user is looking, relative to the device pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/streamingproviderstatus)*