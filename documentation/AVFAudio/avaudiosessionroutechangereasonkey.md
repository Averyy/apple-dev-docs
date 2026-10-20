# AVAudioSessionRouteChangeReasonKey

**Framework**: AVFAudio  
**Kind**: var  
**Role**: Global Variable

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

```c
extern NSString * const AVAudioSessionRouteChangeReasonKey;
```

#### Discussion

The associated value is an unsigned integer, provided as an [`NSNumber`](../Foundation/nsnumber.md) object, that identifies the reason why the route changed. For a list of possible values, see [`AVAudioSession.RouteChangeReason`](./avaudiosession/routechangereason.md).

## See Also

### User info keys
- [let AVAudioSessionRouteChangePreviousRouteKey: String](./avaudiosessionroutechangepreviousroutekey.md)
  A user info key that’s used to retrieve the previously active audio session route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionroutechangereasonkey)*