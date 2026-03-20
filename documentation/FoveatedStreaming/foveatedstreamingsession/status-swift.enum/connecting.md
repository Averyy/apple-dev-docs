# FoveatedStreamingSession.Status.connecting

**Framework**: Foveated Streaming  
**Kind**: case

The session is connecting to a streaming endpoint.

**Availability**:
- visionOS 26.4+

## Declaration

```swift
case connecting
```

#### Discussion

The [`FoveatedStreamingSession`](foveatedstreamingsession.md) enters this state after you call [`connect(endpoint:)`](foveatedstreamingsession/connect(endpoint:).md). When in this state, the person may still be navigating system UI to select an endpoint or scanning a QR code to authenticate the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/status-swift.enum/connecting)*