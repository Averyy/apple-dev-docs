# status

**Framework**: Foveated Streaming  
**Kind**: property  
**Role**: Instance Property

Reports the current status of the foveated streaming provider.

**Availability**:
- visionOS 27.0+

## Declaration

```swift
@MainActor
final var status: FoveatedStreamingProviderStatus { get }
```

#### Discussion

- If the status is `connecting`, then [`connect(context:)`](../foveatedstreamingextension/connect%28context%29.md) is in the middle of being called.
- If the status is `connected`, then [`connect(context:)`](../foveatedstreamingextension/connect%28context%29.md) has completed its call without error.  The stream is assumed running.
- If the status is `disconnecting`, then [`disconnect()`](../foveatedstreamingextension/disconnect%28%29.md) is in the middle of being called.
- If the status is `disconnected`, then [`disconnect()`](../foveatedstreamingextension/disconnect%28%29.md) has completed its call without error.  The stream has been cleanly disconnected.
- If the status is `interrupted`, then [`reportConnectionInterrupted(_:)`](./reportconnectioninterrupted%28_%29.md) has been called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovidercontext/status)*