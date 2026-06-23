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

This may only be called while the provider is in the [`FoveatedStreamingProvider.Status.connected`](foveatedstreamingprovider/status/connected.md) state. Calling this transitions the session to `FoveatedStreamingProvider/Status/error(_:)`.

After calling this method, the provider should consider the session terminated. [`disconnect()`](foveatedstreamingprovider/delegate/disconnect().md) will **not** be called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovider/context/reportconnectioninterrupted(_:))*