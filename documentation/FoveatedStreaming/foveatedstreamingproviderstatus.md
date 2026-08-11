# FoveatedStreamingProviderStatus

**Framework**: Foveated Streaming  
**Kind**: enum

An enum describing the state of a [`FoveatedStreamingExtension`](foveatedstreamingextension.md).

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum FoveatedStreamingProviderStatus
```

## Topics

### Enumeration Cases
- [FoveatedStreamingProviderStatus.connected](foveatedstreamingproviderstatus/connected.md)
  Connected and streaming.
- [FoveatedStreamingProviderStatus.connecting](foveatedstreamingproviderstatus/connecting.md)
  [`connect(context:)`](foveatedstreamingextension/connect(context:).md) is in progress.
- [FoveatedStreamingProviderStatus.disconnected(error:)](foveatedstreamingproviderstatus/disconnected(error:).md)
  The session has been disconnected for the provided reason.
- [FoveatedStreamingProviderStatus.disconnecting](foveatedstreamingproviderstatus/disconnecting.md)
  [`disconnect()`](foveatedstreamingextension/disconnect().md) has been called.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingproviderstatus)*