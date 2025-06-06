# AVAudioSessionRouteChangeReasonKey

**Framework**: AVFAudio  
**Kind**: var

A user info key that’s used to retrieve the route change reason.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let AVAudioSessionRouteChangeReasonKey: String
```

#### Discussion

The associated value is an unsigned integer, provided as an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object, that identifies the reason why the route changed. For a list of possible values, see [`AVAudioSession.RouteChangeReason`](avaudiosession/routechangereason.md).

## See Also

- [let AVAudioSessionRouteChangePreviousRouteKey: String](avaudiosessionroutechangepreviousroutekey.md)
  A user info key that’s used to retrieve the previously active audio session route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionroutechangereasonkey)*