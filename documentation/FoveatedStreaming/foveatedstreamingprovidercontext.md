# FoveatedStreamingProviderContext

**Framework**: Foveated Streaming  
**Kind**: protocol

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol FoveatedStreamingProviderContext : AnyObject, Observable
```

## Topics

### Instance Properties
- [var endpoint: FoveatedStreamingProviderEndpoint](foveatedstreamingprovidercontext/endpoint.md)
  The endpoint for which a connection is being requested (local IP or remote URL).
- [var latestFocusRegion: FocusRegion?](foveatedstreamingprovidercontext/latestfocusregion.md)
  The latest eye input data, to be used to enable foveated streaming.
- [var microphoneEnabled: Bool](foveatedstreamingprovidercontext/microphoneenabled.md)
  A convenience function that reports if microphone support is enabled for the process.
- [var status: StreamingProviderStatus](foveatedstreamingprovidercontext/status.md)
  A convenience function that reports the current status of the foveated streaming provider.
- [var taskIDToken: task_id_token_t](foveatedstreamingprovidercontext/taskidtoken.md)
  A token to be used for billing large buffer allocations to the host app.
### Instance Methods
- [func availableMessageChannelsDidUpdate(Set<String>)](foveatedstreamingprovidercontext/availablemessagechannelsdidupdate(_:).md)
  Notifies the host app that the list of available message channels has updated.
- [func messageChannelDidClose(channelId: String)](foveatedstreamingprovidercontext/messagechanneldidclose(channelid:).md)
  Notifies the host app that a message channel has closed.
- [func messageChannelDidReceiveData(channelId: String, data: Data)](foveatedstreamingprovidercontext/messagechanneldidreceivedata(channelid:data:).md)
  Notifies the host app that a message channel received data.
- [func registerForMemoryAttribution(IOSurface)](foveatedstreamingprovidercontext/registerformemoryattribution(_:)-2wipd.md)
  Attributes an IOSurface’s memory to the host app instead of the extension.
- [func registerForMemoryAttribution(any MTLResource)](foveatedstreamingprovidercontext/registerformemoryattribution(_:)-446ds.md)
  Attributes a Metal resource’s memory to the host app instead of the extension.
- [func reportConnectionInterrupted(any Error)](foveatedstreamingprovidercontext/reportconnectioninterrupted(_:).md)
  Reports that a previously-established connection was unexpectedly lost.

## Relationships

### Inherits From
- [Observable](../Observation/Observable.md)

## See Also

- [func streamingProviderScene<Provider>(providerType: Provider.Type) -> some AppExtensionScene](streamingproviderscene(providertype:).md)
  Creates a complete app extension scene for a foveated streaming provider extension.
- [protocol FoveatedStreamingProvider](foveatedstreamingprovider.md)
  Protocol that streaming provider system extensions must implement.
- [enum FoveatedStreamingProviderEndpoint](foveatedstreamingproviderendpoint.md)
  The streaming endpoint provided to a [`FoveatedStreamingProvider`](foveatedstreamingprovider.md) extension.
- [struct FocusRegion](focusregion.md)
  Eye input data that describes where the end user is looking, relative to the device pose.
- [enum StreamingProviderStatus](streamingproviderstatus.md)
  An enum describing the state of a [`FoveatedStreamingProvider`](foveatedstreamingprovider.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovidercontext)*