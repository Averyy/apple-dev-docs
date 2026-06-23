# FoveatedStreamingProvider

**Framework**: Foveated Streaming  
**Kind**: struct

Protocol that streaming provider system extensions must implement.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency struct FoveatedStreamingProvider
```

#### Overview

This may only be used by App Extensions with the [`Foveated Streaming Provider`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.foveated-streaming-provider) entitlement. To request access for your protocol, visit the entitlement request form [`Requesting the Foveated Streaming Provider Entitlement`](https://developer.apple.comhttps://developer.apple.com/contact/request/foveated-streaming-provider/).

## Topics

### Classes
- [FoveatedStreamingProvider.Context](foveatedstreamingprovider/context.md)
  Context object provided to a streaming provider during initialization.
### Protocols
- [FoveatedStreamingProvider.Delegate](foveatedstreamingprovider/delegate.md)
  Protocol that streaming provider extensions must implement.
### Structures
- [FoveatedStreamingProvider.FocusRegion](foveatedstreamingprovider/focusregion.md)
  Eye input data that describes the approximate region that the end user is looking, relative to the device pose.
### Initializers
- [init<Provider>(delegateType: Provider.Type)](foveatedstreamingprovider/init(delegatetype:).md)
### Enumerations
- [FoveatedStreamingProvider.Endpoint](foveatedstreamingprovider/endpoint.md)
  The streaming endpoint provided to a [`FoveatedStreamingProvider`](foveatedstreamingprovider.md) extension.
- [FoveatedStreamingProvider.Status](foveatedstreamingprovider/status.md)
  An enum describing the state of a [`FoveatedStreamingProvider`](foveatedstreamingprovider.md).

## Relationships

### Conforms To
- [AppExtensionScene](../ExtensionKit/AppExtensionScene.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovider)*