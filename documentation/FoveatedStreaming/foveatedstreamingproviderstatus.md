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
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingproviderstatus)*