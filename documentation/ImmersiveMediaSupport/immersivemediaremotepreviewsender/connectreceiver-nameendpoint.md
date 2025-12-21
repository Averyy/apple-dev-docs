# connectReceiver(name:endpoint:)

**Framework**: Immersive Media Support  
**Kind**: method

Adds an [`ImmersiveMediaRemotePreviewReceiver`](immersivemediaremotepreviewreceiver.md) to the sender as an active participant of the network preview. Any updates on the sender will be propagated to all active receivers (frames, camera information, static metadata).

**Availability**:
- macOS 26.0+

## Declaration

```swift
func connectReceiver(name: String, endpoint: NWEndpoint) async throws
```

#### Discussion

> **Note**: This function throws if anything fails establishing the connection to the receiver..

## Parameters

- `name`: The name associated with the receiver being connected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivemediaremotepreviewsender/connectreceiver(name:endpoint:))*