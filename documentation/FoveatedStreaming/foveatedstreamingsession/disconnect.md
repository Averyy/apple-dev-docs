# disconnect()

**Framework**: Foveated Streaming  
**Kind**: method

Disconnects from the remote streaming endpoint, ending the streaming session.

**Availability**:
- visionOS 26.4+

## Declaration

```swift
@MainActor
final func disconnect() async
```

#### Discussion

When this function returns, the foveated streaming session’s [`status`](foveatedstreamingsession/status-swift.property.md) will equal [`FoveatedStreamingSession.Status.disconnected(_:)`](foveatedstreamingsession/status-swift.enum/disconnected(_:).md) with the reason [`appInitiatedDisconnect`](foveatedstreamingsession/disconnectreason/appinitiateddisconnect.md).

You can reconnect by calling [`connect(endpoint:)`](foveatedstreamingsession/connect(endpoint:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/disconnect())*