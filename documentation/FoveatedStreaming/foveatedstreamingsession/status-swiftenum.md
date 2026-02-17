# FoveatedStreamingSession.Status

**Framework**: Foveated Streaming  
**Kind**: enum

The connection state of a foveated streaming session.

**Availability**:
- visionOS 26.4+ (Beta)

## Declaration

```swift
enum Status
```

## Topics

### Enumeration Cases
- [FoveatedStreamingSession.Status.connected](foveatedstreamingsession/status-swift.enum/connected.md)
  The session is connected and streaming from a streaming endpoint.
- [FoveatedStreamingSession.Status.connecting](foveatedstreamingsession/status-swift.enum/connecting.md)
  The session is connecting to a streaming endpoint.
- [case disconnected(FoveatedStreamingSession.DisconnectReason)](foveatedstreamingsession/status-swift.enum/disconnected(_:).md)
  The session has disconnected or failed to connect to a streaming endpoint.
- [FoveatedStreamingSession.Status.disconnecting](foveatedstreamingsession/status-swift.enum/disconnecting.md)
  The session is disconnecting from a streaming endpoint.
- [FoveatedStreamingSession.Status.initialized](foveatedstreamingsession/status-swift.enum/initialized.md)
  The initial state of the session.
- [FoveatedStreamingSession.Status.paused](foveatedstreamingsession/status-swift.enum/paused.md)
  The session is paused and has temporarily stopped streaming from a streaming endpoint.
- [FoveatedStreamingSession.Status.pausing](foveatedstreamingsession/status-swift.enum/pausing.md)
  The session is pausing its connection to a streaming endpoint.
- [FoveatedStreamingSession.Status.resuming](foveatedstreamingsession/status-swift.enum/resuming.md)
  The session is resuming its connection to a streaming endpoint.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/status-swift.enum)*