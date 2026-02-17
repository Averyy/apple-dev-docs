# FoveatedStreamingSession.Status.disconnected(_:)

**Framework**: Foveated Streaming  
**Kind**: case

The session has disconnected or failed to connect to a streaming endpoint.

**Availability**:
- visionOS 26.4+ (Beta)

## Declaration

```swift
case disconnected(FoveatedStreamingSession.DisconnectReason)
```

#### Discussion

The [`FoveatedStreamingSession`](foveatedstreamingsession.md) enters this state after you call [`disconnect()`](foveatedstreamingsession/disconnect().md) or because the connection has been interrupted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/status-swift.enum/disconnected(_:))*