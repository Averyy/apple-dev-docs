# streamingProviderScene(providerType:)

**Framework**: Foveated Streaming  
**Kind**: func

Creates a complete app extension scene for a foveated streaming provider extension.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
func streamingProviderScene<Provider>(providerType: Provider.Type) -> some AppExtensionScene where Provider : FoveatedStreamingProvider
```

#### Discussion

This may only be used by App Extensions with the `com.apple.developer.foveated-streaming-provider` entitlement.

## See Also

- [protocol FoveatedStreamingProvider](foveatedstreamingprovider.md)
  Protocol that streaming provider system extensions must implement.
- [protocol FoveatedStreamingProviderContext](foveatedstreamingprovidercontext.md)
- [enum FoveatedStreamingProviderEndpoint](foveatedstreamingproviderendpoint.md)
  The streaming endpoint provided to a [`FoveatedStreamingProvider`](foveatedstreamingprovider.md) extension.
- [struct FocusRegion](focusregion.md)
  Eye input data that describes where the end user is looking, relative to the device pose.
- [enum StreamingProviderStatus](streamingproviderstatus.md)
  An enum describing the state of a [`FoveatedStreamingProvider`](foveatedstreamingprovider.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/streamingproviderscene(providertype:))*