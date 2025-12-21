# NSURLRequest.NetworkServiceType.voip

**Framework**: Foundation  
**Kind**: case

A service type for VoIP traffic.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case voip
```

#### Discussion

With the VoIP service type, the kernel continues to listen for incoming traffic while your app is in the background, then wakes up your app whenever new data arrives. Set this  for connections that are communicate with a VoIP service.

## See Also

- [NSURLRequest.NetworkServiceType.default](nsurlrequest/networkservicetype-swift.enum/default.md)
  A service type for standard network traffic.
- [NSURLRequest.NetworkServiceType.video](nsurlrequest/networkservicetype-swift.enum/video.md)
  A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NSURLRequest.NetworkServiceType.background](nsurlrequest/networkservicetype-swift.enum/background.md)
  A service type for high-delay tolerant, high-loss tolerant, elastic flow, and variable size connections.
- [NSURLRequest.NetworkServiceType.voice](nsurlrequest/networkservicetype-swift.enum/voice.md)
  A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NSURLRequest.NetworkServiceType.callSignaling](nsurlrequest/networkservicetype-swift.enum/callsignaling.md)
  A service for low-loss tolerant, inelastic flow, jitter tolerant, short but bursty rate, and variable size connections.
- [NSURLRequest.NetworkServiceType.responsiveData](nsurlrequest/networkservicetype-swift.enum/responsivedata.md)
  A service type for medium-delay tolerant, elastic and inelastic flow, bursty, and long-lived connections.
- [NSURLRequest.NetworkServiceType.avStreaming](nsurlrequest/networkservicetype-swift.enum/avstreaming.md)
  A service type for medium-delay tolerant, low-medium-loss tolerant, elastic flow, constant packet interval, and variable rate and size connections.
- [NSURLRequest.NetworkServiceType.responsiveAV](nsurlrequest/networkservicetype-swift.enum/responsiveav.md)
  A service type for low-delay tolerant, low-to-medium-loss tolerant, elastic flow, variable packet interval, rate, size responsive and time-sensitive connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/networkservicetype-swift.enum/voip)*