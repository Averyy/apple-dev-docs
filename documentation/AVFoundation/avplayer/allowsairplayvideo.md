# allowsAirPlayVideo

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the player allows AirPlay video playback.

**Availability**:
- tvOS 9.0+ - Deprecated in 9.0

> **Deprecated**: Use [`allowsExternalPlayback`](./allowsexternalplayback.md) instead.

## Declaration

```swift
var allowsAirPlayVideo: Bool { get set }
```

```objc
@property BOOL allowsAirPlayVideo;
```

## Discussion

The default value is [`true`](../../Swift/true.md).

## See Also

### Configuring AirPlay behavior
- [var isAirPlayVideoActive: Bool](./isairplayvideoactive.md)
  A Boolean value that indicates whether the player is playing video through AirPlay.
- [var usesAirPlayVideoWhileAirPlayScreenIsActive: Bool](./usesairplayvideowhileairplayscreenisactive.md)
  A Boolean value that indicates whether the player automatically switches to AirPlay Video while AirPlay Screen is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/allowsairplayvideo)*