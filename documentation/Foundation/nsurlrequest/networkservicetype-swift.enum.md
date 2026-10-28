# NSURLRequest.NetworkServiceType

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

Constants that specify how a request uses network resources.

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
enum NetworkServiceType
```

```c
enum NSURLRequestNetworkServiceType : NSUInteger;
```

## Overview

The network service type provides a hint to the operating system about the nature and use of the underlying traffic. This hint enhances the system’s ability to prioritize traffic, determine how quickly it needs to wake up the cellular or Wi-Fi radio, and so on. By providing accurate information, you improve the system’s ability to optimally balance battery life, performance, and other considerations.

Make connections using the [`NSURLRequest.NetworkServiceType.default`](./networkservicetype-swift.enum/default.md) service type.

## Topics

### Network service types
- [NSURLRequest.NetworkServiceType.default](./networkservicetype-swift.enum/default.md)
  A service type for standard network traffic.
- [NSURLRequest.NetworkServiceType.video](./networkservicetype-swift.enum/video.md)
  A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NSURLRequest.NetworkServiceType.background](./networkservicetype-swift.enum/background.md)
  A service type for high-delay tolerant, high-loss tolerant, elastic flow, and variable size connections.
- [NSURLRequest.NetworkServiceType.voice](./networkservicetype-swift.enum/voice.md)
  A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NSURLRequest.NetworkServiceType.callSignaling](./networkservicetype-swift.enum/callsignaling.md)
  A service for low-loss tolerant, inelastic flow, jitter tolerant, short but bursty rate, and variable size connections.
- [NSURLRequest.NetworkServiceType.responsiveData](./networkservicetype-swift.enum/responsivedata.md)
  A service type for medium-delay tolerant, elastic and inelastic flow, bursty, and long-lived connections.
- [NSURLRequest.NetworkServiceType.avStreaming](./networkservicetype-swift.enum/avstreaming.md)
  A service type for medium-delay tolerant, low-medium-loss tolerant, elastic flow, constant packet interval, and variable rate and size connections.
- [NSURLRequest.NetworkServiceType.responsiveAV](./networkservicetype-swift.enum/responsiveav.md)
  A service type for low-delay tolerant, low-to-medium-loss tolerant, elastic flow, variable packet interval, rate, size responsive and time-sensitive connections.
- [NSURLRequest.NetworkServiceType.voip](./networkservicetype-swift.enum/voip.md)
  A service type for VoIP traffic.
### Initializers
- [init?(rawValue: UInt)](./networkservicetype-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing the service type
- [var networkServiceType: NSURLRequest.NetworkServiceType](../nsmutableurlrequest/networkservicetype.md)
  The network service type of the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/networkservicetype-swift.enum)*