# FoveatedStreamingProviderContext

**Framework**: Foveated Streaming  
**Kind**: class

Context object provided to a streaming provider when it connects.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
final class FoveatedStreamingProviderContext
```

#### Overview

Provides access to session state, endpoint information, focus region data, and helpers for communicating events back to the host app.

## Topics

### Instance Properties
- [let endpoint: FoveatedStreamingProviderEndpoint](foveatedstreamingprovidercontext/endpoint.md)
  The endpoint for which a connection is being requested (local IP or remote URL).
- [var immersiveSpaceFromRemoteSpaceTransform: simd_float4x4](foveatedstreamingprovidercontext/immersivespacefromremotespacetransform.md)
  Transform matrix from the remote space to the immersive space.
- [var latestFocusRegion: FoveatedStreamingProviderFocusRegion?](foveatedstreamingprovidercontext/latestfocusregion.md)
  The latest eye input data, to be used to enable foveated streaming.
- [var requestedInputCapabilities: Set<FoveatedStreamingSession.InputCapability>](foveatedstreamingprovidercontext/requestedinputcapabilities.md)
  The set of input capabilities the host app has requested for this session.
- [var status: FoveatedStreamingProviderStatus](foveatedstreamingprovidercontext/status.md)
  Reports the current status of the foveated streaming provider.
### Instance Methods
- [func attributeToHostApp(IOSurface)](foveatedstreamingprovidercontext/attributetohostapp(_:)-50mip.md)
  Attributes an IOSurface’s memory to the host app instead of the extension.
- [func attributeToHostApp(any MTLResource)](foveatedstreamingprovidercontext/attributetohostapp(_:)-88yg7.md)
  Attributes a Metal resource’s memory to the host app instead of the extension.
- [func reportConnectionInterrupted(any Error)](foveatedstreamingprovidercontext/reportconnectioninterrupted(_:).md)
  Reports that a previously-established connection was unexpectedly lost.
- [func updateAvailableMessageChannels([FoveatedStreamingSession.MessageChannel.ID])](foveatedstreamingprovidercontext/updateavailablemessagechannels(_:).md)
  Notifies the host app that the list of available message channels has updated.
- [func verifyRemoteServerTrust(for: URLAuthenticationChallenge) async -> Bool](foveatedstreamingprovidercontext/verifyremoteservertrust(for:).md)
  Verifies the server certificate presented in a TLS authentication challenge.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Escapable](../Swift/Escapable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum FoveatedStreamingProviderEndpoint](foveatedstreamingproviderendpoint.md)
  The streaming endpoint provided to a `FoveatedStreamingProvider` extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovidercontext)*