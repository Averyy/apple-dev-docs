# pause()

**Framework**: Foveated Streaming  
**Kind**: method  
**Role**: Instance Method

Pauses a session without ending it.

**Availability**:
- visionOS 26.4+

## Declaration

```swift
@MainActor
final func pause() async throws
```

## Discussion

> **Throws**: A [`FoveatedStreamingSession.DisconnectReason`](./disconnectreason.md) error if a disconnection occurs.  Or, a [`CancellationError`](../../Swift/cancellationerror.md) if the task is cancelled.

When this function returns successfully without throwing an error the foveated streaming session’s [`status`](./status-swift.property.md) will equal [`FoveatedStreamingSession.Status.paused`](./status-swift.enum/paused.md).

You can resume the session by calling [`resume()`](./resume%28%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/pause())*