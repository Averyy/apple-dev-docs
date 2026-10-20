# resume()

**Framework**: Foveated Streaming  
**Kind**: method  
**Role**: Instance Method

Resumes a previously paused session.

**Availability**:
- visionOS 26.4+

## Declaration

```swift
@MainActor
final func resume() async throws
```

#### Discussion

> **Throws**: A [`FoveatedStreamingSession.DisconnectReason`](./disconnectreason.md) error if a disconnection occurs.  Or, a [`CancellationError`](../../Swift/cancellationerror.md) if the task is cancelled.

When this function returns successfully without throwing an error the foveated streaming session’s [`status`](./status-swift.property.md) will equal [`FoveatedStreamingSession.Status.connected`](./status-swift.enum/connected.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/resume())*