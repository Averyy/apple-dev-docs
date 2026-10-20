# FoveatedStreamingProviderStatus

**Framework**: Foveated Streaming  
**Kind**: enum  
**Role**: Enumeration

An enum describing the state of a [`FoveatedStreamingExtension`](./foveatedstreamingextension.md).

**Availability**:
- visionOS 27.0+

## Declaration

```swift
enum FoveatedStreamingProviderStatus
```

## Topics

### Enumeration Cases
- [FoveatedStreamingProviderStatus.connected](./foveatedstreamingproviderstatus/connected.md)
  Connected and streaming.
- [FoveatedStreamingProviderStatus.connecting](./foveatedstreamingproviderstatus/connecting.md)
  [`connect(context:)`](./foveatedstreamingextension/connect%28context%29.md) is in progress.
- [FoveatedStreamingProviderStatus.disconnected(error:)](./foveatedstreamingproviderstatus/disconnected%28error%29.md)
  The session has been disconnected for the provided reason.
- [FoveatedStreamingProviderStatus.disconnecting](./foveatedstreamingproviderstatus/disconnecting.md)
  [`disconnect()`](./foveatedstreamingextension/disconnect%28%29.md) has been called.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingproviderstatus)*