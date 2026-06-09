# FoveatedStreamingProvider

**Framework**: Foveated Streaming  
**Kind**: protocol

Protocol that streaming provider system extensions must implement.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
protocol FoveatedStreamingProvider
```

#### Overview

This may only be used by App Extensions with the `com.apple.developer.foveated-streaming-provider` entitlement.

## Topics

### Associated Types
- [associatedtype Content : View](foveatedstreamingprovider/content.md)
  The type of the view that renders the streamed content.
### Initializers
- [init(context: any FoveatedStreamingProviderContext) async throws](foveatedstreamingprovider/init(context:).md)
  Initialize the streaming provider and connect to the provided endpoint.
### Instance Properties
- [var immersiveScene: Self.Content](foveatedstreamingprovider/immersivescene.md)
  The SwiftUI view that renders the streamed content.
- [var remoteSceneFromImmersiveSpaceTransform: simd_float4x4](foveatedstreamingprovider/remotescenefromimmersivespacetransform.md)
  Transform matrix from the remote scene’s coordinate space to the immersive space.
### Instance Methods
- [func closeMessageChannel(channelId: String)](foveatedstreamingprovider/closemessagechannel(channelid:).md)
  Closes a message channel.
- [func disconnect() async throws](foveatedstreamingprovider/disconnect.md)
  Disconnect from the streaming endpoint.
- [func openMessageChannel(channelId: String) throws](foveatedstreamingprovider/openmessagechannel(channelid:).md)
  Opens a message channel with the given identifier.
- [func sendDataOnChannel(channelId: String, data: Data) throws](foveatedstreamingprovider/senddataonchannel(channelid:data:).md)
  Sends data on an open message channel.

## See Also

- [func streamingProviderScene<Provider>(providerType: Provider.Type) -> some AppExtensionScene](streamingproviderscene(providertype:).md)
  Creates a complete app extension scene for a foveated streaming provider extension.
- [protocol FoveatedStreamingProviderContext](foveatedstreamingprovidercontext.md)
- [enum FoveatedStreamingProviderEndpoint](foveatedstreamingproviderendpoint.md)
  The streaming endpoint provided to a [`FoveatedStreamingProvider`](foveatedstreamingprovider.md) extension.
- [struct FocusRegion](focusregion.md)
  Eye input data that describes where the end user is looking, relative to the device pose.
- [enum StreamingProviderStatus](streamingproviderstatus.md)
  An enum describing the state of a [`FoveatedStreamingProvider`](foveatedstreamingprovider.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovider)*