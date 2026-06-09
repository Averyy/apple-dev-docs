# status

**Framework**: Foveated Streaming  
**Kind**: property  
**Required**: Yes

A convenience function that reports the current status of the foveated streaming provider.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
var status: StreamingProviderStatus { get }
```

#### Discussion

- If the status is `connecting`, then [`init(context:)`](foveatedstreamingprovider/init(context:).md) is in the middle of being called.
- If the status is `connected`, then [`init(context:)`](foveatedstreamingprovider/init(context:).md) has completed its call without error.  The stream is assumed running.
- If the status is `disconnecting`, then [`disconnect()`](foveatedstreamingprovider/disconnect().md) is in the middle of being called.
- If the status is `disconnected`, then [`disconnect()`](foveatedstreamingprovider/disconnect().md) has completed its call without error.  The stream has been cleanly disconnected.
- If the status is `interrupted`, then [`reportConnectionInterrupted(_:)`](foveatedstreamingprovidercontext/reportconnectioninterrupted(_:).md) has been called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovidercontext/status)*