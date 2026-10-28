# ImmersiveMediaRemotePreviewSender

**Framework**: Immersive Media Support  
**Kind**: class  
**Role**: Class

An observable object that helps an app send the required data to all connected receiver applications to help facilitate the complete preview of the immersive media playback.

**Availability**:
- macOS 26.0+

## Declaration

```swift
class ImmersiveMediaRemotePreviewSender
```

## Overview

Applications have to implement the protocol [`ImmersiveMediaPreviewMessagingProtocol`](./immersivemediapreviewmessagingprotocol.md) so that messages exchanged between sender and receivers are in the correct format for processing. Applications need to provide this as custom protocol when establishing the network connection between the sender and the receivers.

It’s also important to configure the NWParameters to be secure by adding TLS security options as the example below.

```swift
func setupNWParameters() -> NWParameters {
    let tcpOptions = NWProtocolTCP.Options()
    let tls = /* setup TLS security options */

    let ret = NWParameters(tls: tls, tcp: tcpOptions)

    let options = NWProtocolFramer.Options(definition: ImmersiveMediaPreviewMessagingProtocol.definition)
    ret.defaultProtocolStack.applicationProtocols.insert(options, at: 0)

    return ret
}
```

```swift
let parameters = setupNWParameters()
let browser = NWBrowser(for: .bonjour(type: serviceType, domain: nil), using: parameters)
```

```swift
let parameters = setupNWParameters()
let listener = try NWListener(using: parameters)
```

## Topics

### Initializers
- [init(networkParameters: NWParameters?) async throws](./immersivemediaremotepreviewsender/init%28networkparameters%29.md)
  Creates a preview sender using the specified network parameters, if any.
### Instance Properties
- [var connectedReceiverNames: [String]](./immersivemediaremotepreviewsender/connectedreceivernames.md)
  An array with the names of all receives currently receiving data from this instance. When a receiver goes offline, this array will be automatically updated.
- [var isReadyToSendData: Bool](./immersivemediaremotepreviewsender/isreadytosenddata.md)
  A Boolean value that indicates whether this preview sender is ready to send data.
- [var preferredFrameRate: Int](./immersivemediaremotepreviewsender/preferredframerate.md)
  The preferred frame rate to use when sending and previewing frames. This is optional; a value of `-1` enables the system to decide the best framerate based on network quality.
- [var preferredVideoHeight: Int](./immersivemediaremotepreviewsender/preferredvideoheight.md)
  The preferred video height to be used when sending and previewing frames. This is optional; a value of `-1` enables the system to decide the best resolution.
- [var preferredVideoWidth: Int](./immersivemediaremotepreviewsender/preferredvideowidth.md)
  The preferred video width to use when sending and previewing frames. This is optional; a value of `-1` enables the system to decide the best resolution.
### Instance Methods
- [func connectReceiver(name: String, endpoint: NWEndpoint) async throws](./immersivemediaremotepreviewsender/connectreceiver%28name,endpoint%29.md)
  Adds an [`ImmersiveMediaRemotePreviewReceiver`](./immersivemediaremotepreviewreceiver.md) to the sender as an active participant of the network preview. Any updates on the sender will be propagated to all active receivers (frames, camera information, static metadata).
- [func disconnectReceiver(name: String) async](./immersivemediaremotepreviewsender/disconnectreceiver%28name%29.md)
  Disconnects a specific remote preview receiver associated with the name provided when [`connectReceiver(name:endpoint:)`](./immersivemediaremotepreviewsender/connectreceiver%28name,endpoint%29.md) was called.
- [func send(audioBuffer: CMSampleBuffer) async throws](./immersivemediaremotepreviewsender/send%28audiobuffer%29.md)
  Sends an audio frame to all connected receivers.
- [func send(taggedBuffers: [CMTaggedBuffer], presentationTimeStamp: CMTime, frameDuration: CMTime) async throws](./immersivemediaremotepreviewsender/send%28taggedbuffers,presentationtimestamp,frameduration%29.md)
  Sends a video frame to all the connected receivers using its tagged buffers representation.
- [func send(venueDescriptor: VenueDescriptor) async throws](./immersivemediaremotepreviewsender/send%28venuedescriptor%29.md)
  Sends a venue descriptor to all connected receivers.
- [func send(videoBuffer: CMSampleBuffer) async throws](./immersivemediaremotepreviewsender/send%28videobuffer%29.md)
  Sends the video frame to the receivers.
- [func send(videoFrame: ImmersiveVideoFrame, presentationTimeStamp: CMTime, frameDuration: CMTime, metadata: [PresentationCommand]) async throws](./immersivemediaremotepreviewsender/send%28videoframe,presentationtimestamp,frameduration,metadata%29.md)
  Sends a video frame to all the connected receivers using its sample buffer representation.
- [func sendVenueDescriptor(at: URL) async throws](./immersivemediaremotepreviewsender/sendvenuedescriptor%28at%29.md)
  Sends an AIME to all connected receivers.
- [func start() async](./immersivemediaremotepreviewsender/start%28%29.md)
  Starts the sender.
- [func stop() async](./immersivemediaremotepreviewsender/stop%28%29.md)
  Stops the sender - all current connected receivers will be disconnected and streaming will stop.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [Observable](../Observation/observable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Preview
- [class ImmersiveMediaPreviewMessagingProtocol](./immersivemediapreviewmessagingprotocol.md)
  An object that represents the messaging protocol a remote preview sender and receiver use to communicate.
- [class ImmersiveMediaRemotePreviewReceiver](./immersivemediaremotepreviewreceiver.md)
  An observable object that helps applications handle receiving commands and data sent from an immersive media remote preview sender object.
- [class ImmersivePreviewRenderer](./immersivepreviewrenderer.md)
  An object that renders an immersive video frame into a texture and exposes the command buffer for presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivemediaremotepreviewsender)*