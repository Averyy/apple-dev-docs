# disconnect()

**Framework**: Foveated Streaming  
**Kind**: method  
**Role**: Instance Method

Disconnects from the remote streaming endpoint, ending the streaming session.

**Availability**:
- visionOS 26.4+

## Declaration

```swift
@MainActor
final func disconnect() async
```

## Discussion

When this function returns, the foveated streaming session’s [`status`](./status-swift.property.md) will equal [`FoveatedStreamingSession.Status.disconnected(_:)`](./status-swift.enum/disconnected%28_%29.md) with the reason [`appInitiatedDisconnect`](./disconnectreason/appinitiateddisconnect.md).

You can reconnect by calling [`connect(endpoint:)`](./connect%28endpoint%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/disconnect())*