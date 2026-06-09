# reportConnectionInterrupted(_:)

**Framework**: Foveated Streaming  
**Kind**: method  
**Required**: Yes

Reports that a previously-established connection was unexpectedly lost.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
func reportConnectionInterrupted(_ error: any Error)
```

#### Discussion

This may only be called while the provider is in the [`StreamingProviderStatus.connected`](streamingproviderstatus/connected.md) state. Calling this transitions the session to `StreamingProviderStatus/error(_:)`.

After calling this method, the provider should consider the session terminated. [`disconnect()`](foveatedstreamingprovider/disconnect().md) will **not** be called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovidercontext/reportconnectioninterrupted(_:))*