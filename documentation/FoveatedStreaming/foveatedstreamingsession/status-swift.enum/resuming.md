# FoveatedStreamingSession.Status.resuming

**Framework**: Foveated Streaming  
**Kind**: case

The session is resuming its connection to a streaming endpoint.

**Availability**:
- visionOS 26.4+

## Declaration

```swift
case resuming
```

#### Discussion

The [`FoveatedStreamingSession`](foveatedstreamingsession.md) briefly enters this state while it reestablishes a connection with the streaming endpoint after you call  [`resume()`](foveatedstreamingsession/resume().md), or after the person presses the resume button on the system UI presented when the session is paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/status-swift.enum/resuming)*