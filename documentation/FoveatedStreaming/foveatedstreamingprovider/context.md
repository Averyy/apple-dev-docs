# FoveatedStreamingProvider.Context

**Framework**: Foveated Streaming  
**Kind**: class

Context object provided to a streaming provider during initialization.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
final class Context
```

#### Overview

Provides access to session state, endpoint information, focus region data, and helpers for communicating events back to the host app.

## Topics

### Instance Properties
- [let endpoint: FoveatedStreamingProvider.Endpoint](foveatedstreamingprovider/context/endpoint.md)
  The endpoint for which a connection is being requested (local IP or remote URL).
- [var latestFocusRegion: FoveatedStreamingProvider.FocusRegion?](foveatedstreamingprovider/context/latestfocusregion.md)
  The latest eye input data, to be used to enable foveated streaming.
- [var requestedInputCapabilities: Set<FoveatedStreamingSession.InputCapability>](foveatedstreamingprovider/context/requestedinputcapabilities.md)
  The set of input capabilities the host app has requested for this session.
- [var status: FoveatedStreamingProvider.Status](foveatedstreamingprovider/context/status.md)
  Reports the current status of the foveated streaming provider.
### Instance Methods
- [func attributeToHostApp(IOSurface)](foveatedstreamingprovider/context/attributetohostapp(_:)-298bm.md)
  Attributes an IOSurface’s memory to the host app instead of the extension.
- [func attributeToHostApp(any MTLResource)](foveatedstreamingprovider/context/attributetohostapp(_:)-8ca4q.md)
  Attributes a Metal resource’s memory to the host app instead of the extension.
- [func closeMessageChannel(channelID: FoveatedStreamingSession.MessageChannel.ID)](foveatedstreamingprovider/context/closemessagechannel(channelid:).md)
  Notifies the host app that a message channel has closed.
- [func receive(Data, onChannel: FoveatedStreamingSession.MessageChannel.ID)](foveatedstreamingprovider/context/receive(_:onchannel:).md)
  Notifies the host app that a message channel received data.
- [func reportConnectionInterrupted(any Error)](foveatedstreamingprovider/context/reportconnectioninterrupted(_:).md)
  Reports that a previously-established connection was unexpectedly lost.
- [func updateAvailableMessageChannels([FoveatedStreamingSession.MessageChannel.ID])](foveatedstreamingprovider/context/updateavailablemessagechannels(_:).md)
  Notifies the host app that the list of available message channels has updated.
- [func verifyRemoteServerTrust(for: URLAuthenticationChallenge) async -> Bool](foveatedstreamingprovider/context/verifyremoteservertrust(for:).md)
  Verifies the server certificate presented in a TLS authentication challenge.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Escapable](../Swift/Escapable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovider/context)*