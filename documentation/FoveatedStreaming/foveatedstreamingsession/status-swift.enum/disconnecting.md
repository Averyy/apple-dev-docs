# FoveatedStreamingSession.Status.disconnecting

**Framework**: Foveated Streaming  
**Kind**: case  
**Role**: Case

The session is disconnecting from a streaming endpoint.

**Availability**:
- visionOS 26.4+

## Declaration

```swift
case disconnecting
```

## Discussion

The [`FoveatedStreamingSession`](../../foveatedstreamingsession.md) briefly enters this state after you call [`disconnect()`](../disconnect%28%29.md) while it completes the disconnection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/status-swift.enum/disconnecting)*