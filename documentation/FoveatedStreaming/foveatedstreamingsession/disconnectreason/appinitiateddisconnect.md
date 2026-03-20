# appInitiatedDisconnect

**Framework**: Foveated Streaming  
**Kind**: property

A disconnect reason indicating the disconnect was initiated by the application.

**Availability**:
- visionOS 26.4+

## Declaration

```swift
static var appInitiatedDisconnect: FoveatedStreamingSession.DisconnectReason { get }
```

#### Discussion

This disconnect reason is given after you call [`disconnect()`](foveatedstreamingsession/disconnect().md), or when the person disconnects from the streaming session via system UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/disconnectreason/appinitiateddisconnect)*