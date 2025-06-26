# ImmersiveMediaRemotePreviewReceiver

**Framework**: Immersive Media Support  
**Kind**: class

An observable object that helps application to handle receiving of the commands and data sent from the immersive media remote preview sender object.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class ImmersiveMediaRemotePreviewReceiver
```

#### Overview

This object helps applications receiving Immersive Video over the network with the intent of rendering a preview playback.

In order to be able to properly render a Immersive Video preview,  the receiver will also have access to:

- The current [`ImmersiveVideoFrame`](immersivevideoframe.md) to be rendered
- The current [`VenueDescriptor`](venuedescriptor.md) to be used for rendering.
- The current [`PresentationDescriptor`](presentationdescriptor.md) describing one or more [`PresentationCommand`](presentationcommand.md)active for the current frame.

## Topics

### Initializers
- [init() async throws](immersivemediaremotepreviewreceiver/init.md)
  Creates a preview receiver object.
### Instance Properties
- [var frame: ImmersiveVideoFrame?](immersivemediaremotepreviewreceiver/frame.md)
  The current remote preview Immersive Video frame.
- [var presentationDescriptor: PresentationDescriptor?](immersivemediaremotepreviewreceiver/presentationdescriptor.md)
  The current remote Immersive Video presentation descriptor - it will contain commands to be processed when displaying the current frame
- [var states: some AsyncSequence<ImmersiveMediaRemotePreviewReceiver.Status, Never>](immersivemediaremotepreviewreceiver/states.md)
  The states that can be used to monitor the current state of the preview receiver so the application can monitor events.
- [var venueDescriptor: VenueDescriptor?](immersivemediaremotepreviewreceiver/venuedescriptor.md)
  The current remote Immersive Video venue descriptor
### Instance Methods
- [func start(connection: NWConnection) async throws](immersivemediaremotepreviewreceiver/start(connection:).md)
  Performs the necessary steps to start receiving remote Immersive Video frames using the given network connection.
- [func stop()](immersivemediaremotepreviewreceiver/stop.md)
  Stops receiving remote Immersive Video frames.
### Enumerations
- [ImmersiveMediaRemotePreviewReceiver.Status](immersivemediaremotepreviewreceiver/status.md)
  A value representing the status of the immersive media remote preview receiver object.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivemediaremotepreviewreceiver)*