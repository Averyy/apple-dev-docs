# pause()

**Framework**: Foveated Streaming  
**Kind**: method

Pauses a session without ending it.

**Availability**:
- visionOS 26.4+ (Beta)

## Declaration

```swift
@MainActor
final func pause() async throws
```

#### Discussion

> **Note**: A [`FoveatedStreamingSession.DisconnectReason`](foveatedstreamingsession/disconnectreason.md) error if a disconnection occurs.  Or, a [`CancellationError`](https://developer.apple.com/documentation/Swift/CancellationError) if the task is cancelled.

When this function returns successfully without throwing an error the foveated streaming session’s [`status`](foveatedstreamingsession/status-swift.property.md) will equal [`FoveatedStreamingSession.Status.paused`](foveatedstreamingsession/status-swift.enum/paused.md).

You can resume the session by calling [`resume()`](foveatedstreamingsession/resume().md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/pause())*