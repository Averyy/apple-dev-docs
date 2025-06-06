# AVAudioSessionRouteChangePreviousRouteKey

**Framework**: AVFAudio  
**Kind**: var

A user info key that’s used to retrieve the previously active audio session route.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let AVAudioSessionRouteChangePreviousRouteKey: String
```

#### Discussion

The value for this key is an [`AVAudioSessionRouteDescription`](avaudiosessionroutedescription.md) object that describes the audio route settings prior to the route change.

## See Also

- [let AVAudioSessionRouteChangeReasonKey: String](avaudiosessionroutechangereasonkey.md)
  A user info key that’s used to retrieve the route change reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionroutechangepreviousroutekey)*