# ImmersiveMediaRemotePreviewReceiver

**Framework**: Immersive Media Support  
**Kind**: class

An observable object that helps apps handle receiving commands and data sent from an immersive media remote preview sender object.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class ImmersiveMediaRemotePreviewReceiver
```

#### Overview

This object helps applications receiving Immersive Video over the network with the intent of rendering a preview playback.

To properly render an immersive video preview, the receiver also needs access to:

- The current [`ImmersiveVideoFrame`](immersivevideoframe.md) to render.
- The current [`VenueDescriptor`](venuedescriptor.md) for rendering.
- The current [`PresentationDescriptor`](presentationdescriptor.md) that describes one or more [`PresentationCommand`](presentationcommand.md)instances active for the current frame.

## Topics

### Initializers
- [init() async throws](immersivemediaremotepreviewreceiver/init.md)
  Creates a preview receiver object.
### Instance Properties
- [var frame: ImmersiveVideoFrame?](immersivemediaremotepreviewreceiver/frame.md)
  The current remote preview of an immersive video frame.
- [var presentationDescriptor: PresentationDescriptor?](immersivemediaremotepreviewreceiver/presentationdescriptor.md)
  The current remote immersive video presentation descriptor.
- [var states: some AsyncSequence<ImmersiveMediaRemotePreviewReceiver.Status, Never>](immersivemediaremotepreviewreceiver/states.md)
  The states to use for monitoring the current state of the preview receiver so the app can monitor events.
- [var venueDescriptor: VenueDescriptor?](immersivemediaremotepreviewreceiver/venuedescriptor.md)
  The current remote immersive video venue descriptor.
### Instance Methods
- [func start(connection: NWConnection) async throws](immersivemediaremotepreviewreceiver/start(connection:).md)
  Performs the necessary steps to start receiving remote Immersive video frames using the given network connection.
- [func stop()](immersivemediaremotepreviewreceiver/stop.md)
  Stops receiving remote immersive video frames.
### Enumerations
- [ImmersiveMediaRemotePreviewReceiver.Status](immersivemediaremotepreviewreceiver/status.md)
  A value that represents the status of the immersive media remote preview receiver object.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivemediaremotepreviewreceiver)*