# FoveatedStreamingSession.Status.paused

**Framework**: Foveated Streaming  
**Kind**: case

The session is paused and has temporarily stopped streaming from a streaming endpoint.

**Availability**:
- visionOS 26.4+ (Beta)

## Declaration

```swift
case paused
```

#### Discussion

This state is similar to [`FoveatedStreamingSession.Status.disconnected(_:)`](foveatedstreamingsession/status-swift.enum/disconnected(_:).md), except that reconnecting to the streaming endpoint from this state gaurantees that the person doesn’t have to re-pair with the streaming endpoint.

You can reconnect to the streaming endpoint from this state by calling [`resume()`](foveatedstreamingsession/resume().md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/status-swift.enum/paused)*