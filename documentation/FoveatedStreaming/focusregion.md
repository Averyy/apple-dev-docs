# FocusRegion

**Framework**: Foveated Streaming  
**Kind**: struct

Eye input data that describes where the end user is looking, relative to the device pose.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct FocusRegion
```

## Topics

### Initializers
- [init(direction: simd_float3, distance: Float, timestamp: TimeInterval)](focusregion/init(direction:distance:timestamp:).md)
### Instance Properties
- [var direction: simd_float3](focusregion/direction.md)
  The direction of the user’s gaze in device-relative coordinates.
- [var distance: Float](focusregion/distance.md)
  The estimated distance to the user’s focal point, in meters.
- [var timestamp: TimeInterval](focusregion/timestamp.md)
  The timestamp at which this focus region sample was captured, measured as system uptime in seconds.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func streamingProviderScene<Provider>(providerType: Provider.Type) -> some AppExtensionScene](streamingproviderscene(providertype:).md)
  Creates a complete app extension scene for a foveated streaming provider extension.
- [protocol FoveatedStreamingProvider](foveatedstreamingprovider.md)
  Protocol that streaming provider system extensions must implement.
- [protocol FoveatedStreamingProviderContext](foveatedstreamingprovidercontext.md)
- [enum FoveatedStreamingProviderEndpoint](foveatedstreamingproviderendpoint.md)
  The streaming endpoint provided to a [`FoveatedStreamingProvider`](foveatedstreamingprovider.md) extension.
- [enum StreamingProviderStatus](streamingproviderstatus.md)
  An enum describing the state of a [`FoveatedStreamingProvider`](foveatedstreamingprovider.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/focusregion)*