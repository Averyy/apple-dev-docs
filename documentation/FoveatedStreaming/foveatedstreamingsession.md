# FoveatedStreamingSession

**Framework**: Foveated Streaming  
**Kind**: class

A session that manages a foveated streaming connection to a local or remote streaming endpoint.

**Availability**:
- visionOS 26.4+ (Beta)

## Declaration

```swift
@MainActor
final class FoveatedStreamingSession
```

## Mentions

- [Streaming a CloudXR application to Apple Vision Pro with foveation](streaming-a-cloudxr-application-to-apple-vision-pro-with-foveation.md)

#### Overview

Use `FoveatedStreamingSession` to establish and manage streaming connections from Apple Vision Pro to local or remote endpoints. The session handles connection life cycle, monitors streaming status, and provides access to bidirectional message channels for custom data exchange.

You create a `FoveatedStreamingSession` object directly, typically on app initialization. After creating your session object, use it to initialize the [`FoveatedStreamingSpace`](foveatedstreamingspace.md) that displays the streamed content. To begin streaming spatial content, call the [`connect(endpoint:)`](foveatedstreamingsession/connect(endpoint:).md) function. The connection will fail if your app doesn’t have the [`com.apple.developer.foveated-streaming-session`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.foveated-streaming-session) entitlement.

The following example shows how to connect to a stream and present its content in an immersive space:

```swift
struct FoveatedStreamingApp: App {
    let session = FoveatedStreamingSession()

    var body: some Scene {
        WindowGroup {
            Button("Connect") {
                Task {
                    try await session.connect(endpoint: .systemDiscovered)
                }
            }
        }

        FoveatedStreamingSpace(session: session) {}
    }
}
```

## Topics

### Classes
- [FoveatedStreamingSession.MessageChannel](foveatedstreamingsession/messagechannel.md)
  A bidirectional channel for sending and receiving custom data.
### Structures
- [FoveatedStreamingSession.DisconnectReason](foveatedstreamingsession/disconnectreason.md)
  A description of why a foveated streaming session’s status is in the disconnected state.
- [FoveatedStreamingSession.Endpoint](foveatedstreamingsession/endpoint.md)
  A streaming endpoint that a foveated streaming session can connect to.
- [FoveatedStreamingSession.ImmersivePresentationBehaviors](foveatedstreamingsession/immersivepresentationbehaviors-swift.struct.md)
  The presentation behaviors describing when the immersive space that hosts the streamed content is presented and dismissed.
### Initializers
- [init()](foveatedstreamingsession/init.md)
  Initializes the FoveatedStreamingSession.
### Instance Properties
- [var availableMessageChannels: Set<FoveatedStreamingSession.MessageChannel.ID>](foveatedstreamingsession/availablemessagechannels.md)
  A list of all available message channels in this session.
- [let id: FoveatedStreamingSession.ID](foveatedstreamingsession/id.md)
  A unique identifier for the session.
- [var immersivePresentationBehaviors: FoveatedStreamingSession.ImmersivePresentationBehaviors](foveatedstreamingsession/immersivepresentationbehaviors-swift.property.md)
  An optional set of behaviors which assist in automatically presenting the session’s immersive space.
- [var immersiveSpaceFromRemoteSceneTransform: simd_float4x4](foveatedstreamingsession/immersivespacefromremotescenetransform.md)
  A transform matrix which maps from the streamed scene’s coordinate space origin to the origin of the app’s immersive space.
- [var status: FoveatedStreamingSession.Status](foveatedstreamingsession/status-swift.property.md)
  The connection status of the session.
### Instance Methods
- [func connect(endpoint: FoveatedStreamingSession.Endpoint) async throws](foveatedstreamingsession/connect(endpoint:).md)
  Establishes a streaming connection at the provided endpoint.
- [func disconnect() async](foveatedstreamingsession/disconnect.md)
  Disconnects from the remote streaming endpoint, ending the streaming session.
- [func getMessageChannel(FoveatedStreamingSession.MessageChannel.ID) -> FoveatedStreamingSession.MessageChannel?](foveatedstreamingsession/getmessagechannel(_:).md)
  Creates or retrieves a message channel for the given message channel ID.
- [func pause() async throws](foveatedstreamingsession/pause.md)
  Pauses a session without ending it.
- [func resume() async throws](foveatedstreamingsession/resume.md)
  Resumes a previously paused session.
### Enumerations
- [FoveatedStreamingSession.Status](foveatedstreamingsession/status-swift.enum.md)
  The connection state of a foveated streaming session.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Escapable](../Swift/Escapable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct FoveatedStreamingSpace](foveatedstreamingspace.md)
  An immersive space that displays foveated streaming content.
- [struct OpenFoveatedStreamingSpaceAction](openfoveatedstreamingspaceaction.md)
  An action that presents a foveated streaming space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession)*