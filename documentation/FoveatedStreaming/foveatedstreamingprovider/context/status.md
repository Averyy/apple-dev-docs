# status

**Framework**: Foveated Streaming  
**Kind**: property

Reports the current status of the foveated streaming provider.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
final var status: FoveatedStreamingProvider.Status { get }
```

#### Discussion

- If the status is `connecting`, then `FoveatedStreamingProvider/init(context:)` is in the middle of being called.
- If the status is `connected`, then `FoveatedStreamingProvider/init(context:)` has completed its call without error.  The stream is assumed running.
- If the status is `disconnecting`, then `FoveatedStreamingProvider/disconnect()` is in the middle of being called.
- If the status is `disconnected`, then `FoveatedStreamingProvider/disconnect()` has completed its call without error.  The stream has been cleanly disconnected.
- If the status is `interrupted`, then `FoveatedStreamingProviderContext/reportConnectionInterrupted(_:)` has been called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovider/context/status)*