# FoveatedStreamingSession.Status.pausing

**Framework**: Foveated Streaming  
**Kind**: case

The session is pausing its connection to a streaming endpoint.

**Availability**:
- visionOS 26.4+ (Beta)

## Declaration

```swift
case pausing
```

#### Discussion

The [`FoveatedStreamingSession`](foveatedstreamingsession.md) briefly enters this state while it pauses the connection after you call [`pause()`](foveatedstreamingsession/pause().md), or the person returned to the home screen on visionOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/status-swift.enum/pausing)*