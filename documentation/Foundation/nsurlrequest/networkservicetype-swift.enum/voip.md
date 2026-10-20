# NSURLRequest.NetworkServiceType.voip

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

A service type for VoIP traffic.

**Availability**:
- iOS 4.0+ - Deprecated in 13.0
- iPadOS 4.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.7+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 6.0

> **Deprecated**: This service type has been depreciated, use service type [`NSURLRequest.NetworkServiceType.voice`](./voice.md) instead.

## Declaration

```swift
case voip
```

```c
NSURLNetworkServiceTypeVoIP
```

#### Discussion

With the VoIP service type, the kernel continues to listen for incoming traffic while your app is in the background, then wakes up your app whenever new data arrives. Set this *only* for connections that are communicate with a VoIP service.

## See Also

### Network service types
- [NSURLRequest.NetworkServiceType.default](./default.md)
  A service type for standard network traffic.
- [NSURLRequest.NetworkServiceType.video](./video.md)
  A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NSURLRequest.NetworkServiceType.background](./background.md)
  A service type for high-delay tolerant, high-loss tolerant, elastic flow, and variable size connections.
- [NSURLRequest.NetworkServiceType.voice](./voice.md)
  A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NSURLRequest.NetworkServiceType.callSignaling](./callsignaling.md)
  A service for low-loss tolerant, inelastic flow, jitter tolerant, short but bursty rate, and variable size connections.
- [NSURLRequest.NetworkServiceType.responsiveData](./responsivedata.md)
  A service type for medium-delay tolerant, elastic and inelastic flow, bursty, and long-lived connections.
- [NSURLRequest.NetworkServiceType.avStreaming](./avstreaming.md)
  A service type for medium-delay tolerant, low-medium-loss tolerant, elastic flow, constant packet interval, and variable rate and size connections.
- [NSURLRequest.NetworkServiceType.responsiveAV](./responsiveav.md)
  A service type for low-delay tolerant, low-to-medium-loss tolerant, elastic flow, variable packet interval, rate, size responsive and time-sensitive connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/networkservicetype-swift.enum/voip)*