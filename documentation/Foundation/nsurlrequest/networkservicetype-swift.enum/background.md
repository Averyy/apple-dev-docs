# NSURLRequest.NetworkServiceType.background

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

A service type for high-delay tolerant, high-loss tolerant, elastic flow, and variable size connections.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case background
```

```c
NSURLNetworkServiceTypeBackground
```

#### Discussion

An example of this service type is prefetching content so that it’s available when the user chooses to view it.

## See Also

### Network service types
- [NSURLRequest.NetworkServiceType.default](./default.md)
  A service type for standard network traffic.
- [NSURLRequest.NetworkServiceType.video](./video.md)
  A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
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
- [NSURLRequest.NetworkServiceType.voip](./voip.md)
  A service type for VoIP traffic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/networkservicetype-swift.enum/background)*