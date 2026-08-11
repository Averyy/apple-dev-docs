# reportConnectionInterrupted(_:)

**Framework**: Foveated Streaming  
**Kind**: method

Reports that a previously-established connection was unexpectedly lost.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
final func reportConnectionInterrupted(_ error: any Error)
```

#### Discussion

This may only be called while the provider is in the [`FoveatedStreamingProviderStatus.connected`](foveatedstreamingproviderstatus/connected.md) state. Calling this transitions the session to `FoveatedStreamingProviderStatus/error(_:)`.

After calling this method, the provider should consider the session terminated. [`disconnect()`](foveatedstreamingextension/disconnect().md) will **not** be called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovidercontext/reportconnectioninterrupted(_:))*