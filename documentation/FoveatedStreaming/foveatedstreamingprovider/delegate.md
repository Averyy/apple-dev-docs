# FoveatedStreamingProvider.Delegate

**Framework**: Foveated Streaming  
**Kind**: protocol

Protocol that streaming provider extensions must implement.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
protocol Delegate
```

#### Overview

Extensions implementing this protocol run in a separate process from the host app.

## Topics

### Associated Types
- [associatedtype Content : View](foveatedstreamingprovider/delegate/content.md)
  The type of the view that renders the streamed content.
### Initializers
- [init(context: FoveatedStreamingProvider.Context) async throws](foveatedstreamingprovider/delegate/init(context:).md)
  Initialize the streaming provider and connect to the provided endpoint.
### Instance Properties
- [var immersiveScene: Self.Content](foveatedstreamingprovider/delegate/immersivescene.md)
  The SwiftUI view that renders the streamed content.
- [var immersiveSpaceFromRemoteSceneTransform: simd_float4x4](foveatedstreamingprovider/delegate/immersivespacefromremotescenetransform.md)
  Transform matrix from the remote scene’s coordinate space to the immersive space.
### Instance Methods
- [func closeMessageChannel(channelID: FoveatedStreamingSession.MessageChannel.ID)](foveatedstreamingprovider/delegate/closemessagechannel(channelid:).md)
  Closes a message channel.
- [func disconnect() async throws](foveatedstreamingprovider/delegate/disconnect.md)
  Disconnect from the streaming endpoint.
- [func openMessageChannel(channelID: FoveatedStreamingSession.MessageChannel.ID) throws](foveatedstreamingprovider/delegate/openmessagechannel(channelid:).md)
  Opens a message channel with the given identifier.
- [func send(Data, onChannel: FoveatedStreamingSession.MessageChannel.ID) throws](foveatedstreamingprovider/delegate/send(_:onchannel:).md)
  Sends data on an open message channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovider/delegate)*