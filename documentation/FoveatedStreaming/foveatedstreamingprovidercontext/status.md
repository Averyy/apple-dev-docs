# status

**Framework**: Foveated Streaming  
**Kind**: property

Reports the current status of the foveated streaming provider.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
final var status: FoveatedStreamingProviderStatus { get }
```

#### Discussion

- If the status is `connecting`, then [`connect(context:)`](foveatedstreamingextension/connect(context:).md) is in the middle of being called.
- If the status is `connected`, then [`connect(context:)`](foveatedstreamingextension/connect(context:).md) has completed its call without error.  The stream is assumed running.
- If the status is `disconnecting`, then [`disconnect()`](foveatedstreamingextension/disconnect().md) is in the middle of being called.
- If the status is `disconnected`, then [`disconnect()`](foveatedstreamingextension/disconnect().md) has completed its call without error.  The stream has been cleanly disconnected.
- If the status is `interrupted`, then [`reportConnectionInterrupted(_:)`](foveatedstreamingprovidercontext/reportconnectioninterrupted(_:).md) has been called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovidercontext/status)*