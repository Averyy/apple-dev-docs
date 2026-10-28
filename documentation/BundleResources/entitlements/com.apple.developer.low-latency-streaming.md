# Low-Latency Streaming

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value indicating whether your app may use low-latency wireless networking.

**Availability**:
- visionOS 26.0+

## Details

- **Name**: `com.apple.developer.low-latency-streaming`
- **Type**: boolean



**Default**: `NO`

## Discussion

This entitlement is intended for applications consuming streamed game content on visionOS. The system activates this mode if it has enough resources available.

## See Also

### visionOS
- [Foveated Streaming Session](./com.apple.developer.foveated-streaming-session.md)
  An entitlement that allows a visionOS app to initiate real-time streaming of spatial content from a cloud streaming endpoint via the Foveated Streaming framework.
- [Foveated Streaming Provider](./com.apple.developer.foveated-streaming-provider.md)
  An entitlement that allows other apps to use privacy-sensitive foveation data for streaming from remote endpoints to Apple Vision Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.low-latency-streaming)*