# resume()

**Framework**: Foveated Streaming  
**Kind**: method

Resumes a previously paused session.

**Availability**:
- visionOS 26.4+

## Declaration

```swift
@MainActor
final func resume() async throws
```

#### Discussion

> **Note**: A [`FoveatedStreamingSession.DisconnectReason`](foveatedstreamingsession/disconnectreason.md) error if a disconnection occurs.  Or, a [`CancellationError`](https://developer.apple.com/documentation/Swift/CancellationError) if the task is cancelled.

When this function returns successfully without throwing an error the foveated streaming session’s [`status`](foveatedstreamingsession/status-swift.property.md) will equal [`FoveatedStreamingSession.Status.connected`](foveatedstreamingsession/status-swift.enum/connected.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/resume())*