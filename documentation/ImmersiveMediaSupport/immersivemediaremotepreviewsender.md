# ImmersiveMediaRemotePreviewSender

**Framework**: Immersive Media Support  
**Kind**: class

An observable object that can help the application to send all the required data to all the connected receiver applications to help facilitate the complete preview of the immersive media playback.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
class ImmersiveMediaRemotePreviewSender
```

#### Overview

The applications have to implement the protocol [`ImmersiveMediaPreviewMessagingProtocol`](immersivemediapreviewmessagingprotocol.md) so that messages exchanged between sender and receivers can be in the correct format for processing. The applications need to provide this as custom protocol when they establish the network connection between the sender and the receivers.

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
- [init(networkParameters: NWParameters?) async throws](immersivemediaremotepreviewsender/init(networkparameters:).md)
  Creates a preview sender using the specified network parameters, if any.
### Instance Properties
- [var connectedReceiverNames: [String]](immersivemediaremotepreviewsender/connectedreceivernames.md)
  An array with the names of all receives currently receiving data from this instance. When a receiver goes offline, this array will be automatically updated.
- [var isReadyToSendData: Bool](immersivemediaremotepreviewsender/isreadytosenddata.md)
  A Boolean value that indicates whether this preview sender is ready to send data or not.
- [var preferredFrameRate: Int](immersivemediaremotepreviewsender/preferredframerate.md)
  The preferred frame rate to be used when sending and previewing frames. This is optional and a value of -1 will let the system decide the best framerate to use based on network quality.
- [var preferredVideoHeight: Int](immersivemediaremotepreviewsender/preferredvideoheight.md)
  The preferred video height to be used when sending and previewing frames. This is optional and a value of -1 will let the system decide the best resolution to use.
- [var preferredVideoWidth: Int](immersivemediaremotepreviewsender/preferredvideowidth.md)
  The preferred video width to be used when sending and previewing frames. This is optional and a value of -1 will let the system decide the best resolution to use.
### Instance Methods
- [func connectReceiver(name: String, endpoint: NWEndpoint) async throws](immersivemediaremotepreviewsender/connectreceiver(name:endpoint:).md)
  Adds an [`ImmersiveMediaRemotePreviewReceiver`](immersivemediaremotepreviewreceiver.md) to the sender as an active participant of the network preview. Any updates on the sender will be propagated to all active receivers (frames, camera information, static metadata).
- [func disconnectReceiver(name: String) async](immersivemediaremotepreviewsender/disconnectreceiver(name:).md)
  Disconnects a specific remote preview receiver associated with the name provided when [`connectReceiver(name:endpoint:)`](immersivemediaremotepreviewsender/connectreceiver(name:endpoint:).md) was called.
- [func send(audioBuffer: CMSampleBuffer) async throws](immersivemediaremotepreviewsender/send(audiobuffer:).md)
  Sends an audio frame to all connected receivers.
- [func send(taggedBuffers: [CMTaggedBuffer], presentationTimeStamp: CMTime, frameDuration: CMTime) async throws](immersivemediaremotepreviewsender/send(taggedbuffers:presentationtimestamp:frameduration:).md)
  Sends a video frame to all the connected receivers using its tagged buffers representation.
- [func send(venueDescriptor: VenueDescriptor) async throws](immersivemediaremotepreviewsender/send(venuedescriptor:).md)
  Sends a VenueDescriptor to all connected receivers.
- [func send(videoBuffer: CMSampleBuffer) async throws](immersivemediaremotepreviewsender/send(videobuffer:).md)
  Sends the video frame to the receivers.
- [func send(videoFrame: ImmersiveVideoFrame, presentationTimeStamp: CMTime, frameDuration: CMTime, metadata: [PresentationCommand]) async throws](immersivemediaremotepreviewsender/send(videoframe:presentationtimestamp:frameduration:metadata:).md)
  Sends a video frame to all the connected receivers using its sample buffer representation.
- [func sendVenueDescriptor(at: URL) async throws](immersivemediaremotepreviewsender/sendvenuedescriptor(at:).md)
  Sends an AIME (VenueDescriptor file) to all connected receivers.
- [func start() async](immersivemediaremotepreviewsender/start.md)
  Starts the sender - this needs to be called before starting to send frames, audio or venue descriptor information to receivers. After `start` is called, the application should observe the `isReadyForData` property to know when to start sending frames.
- [func stop() async](immersivemediaremotepreviewsender/stop.md)
  Stops the sender - all current connected receivers will be disconnected and streaming will stop.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivemediaremotepreviewsender)*