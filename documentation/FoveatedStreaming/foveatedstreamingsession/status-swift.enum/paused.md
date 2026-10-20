# FoveatedStreamingSession.Status.paused

**Framework**: Foveated Streaming  
**Kind**: case  
**Role**: Case

The session is paused and has temporarily stopped streaming from a streaming endpoint.

**Availability**:
- visionOS 26.4+

## Declaration

```swift
case paused
```

#### Discussion

This state is similar to [`FoveatedStreamingSession.Status.disconnected(_:)`](./disconnected%28_%29.md), except that reconnecting to the streaming endpoint from this state gaurantees that the person doesn’t have to re-pair with the streaming endpoint.

You can reconnect to the streaming endpoint from this state by calling [`resume()`](../resume%28%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/status-swift.enum/paused)*