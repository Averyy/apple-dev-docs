# voIP

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Specifies that the stream is providing VoIP service.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

> **Deprecated**: This legacy VoIP API was deprecated in iOS 10.0. Use [PushKit](../../PushKit/PushKit.md) to develop VoIP apps.

## Declaration

```swift
static let voIP: StreamNetworkServiceTypeValue
```

```c
extern NSStreamNetworkServiceTypeValue const NSStreamNetworkServiceTypeVoIP;
```

## See Also

### Type Properties
- [static let background: StreamNetworkServiceTypeValue](./background.md)
  Specifies that the stream is providing a background service.
- [static let video: StreamNetworkServiceTypeValue](./video.md)
  Specifies that the stream is providing video service.
- [static let voice: StreamNetworkServiceTypeValue](./voice.md)
  Specifies that the stream is providing voice service.
- [static let callSignaling: StreamNetworkServiceTypeValue](./callsignaling.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/streamnetworkservicetypevalue/voip)*