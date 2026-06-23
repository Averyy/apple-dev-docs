# FoveatedStreamingProvider.Status

**Framework**: Foveated Streaming  
**Kind**: enum

An enum describing the state of a [`FoveatedStreamingProvider`](foveatedstreamingprovider.md).

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum Status
```

## Topics

### Enumeration Cases
- [FoveatedStreamingProvider.Status.connected](foveatedstreamingprovider/status/connected.md)
  Connected and streaming.
- [FoveatedStreamingProvider.Status.connecting](foveatedstreamingprovider/status/connecting.md)
  `FoveatedStreamingProvider/init(context:)` is in progress.
- [FoveatedStreamingProvider.Status.disconnected(error:)](foveatedstreamingprovider/status/disconnected(error:).md)
  The session has been disconnected for the provided reason.
- [FoveatedStreamingProvider.Status.disconnecting](foveatedstreamingprovider/status/disconnecting.md)
  `FoveatedStreamingProvider/disconnect()` has been called.

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

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovider/status)*