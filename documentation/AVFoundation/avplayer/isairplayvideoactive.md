# isAirPlayVideoActive

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the player is playing video through AirPlay.

**Availability**:
- tvOS 9.0+ - Deprecated in 9.0

> **Deprecated**: Use [`isExternalPlaybackActive`](./isexternalplaybackactive.md) instead.

## Declaration

```swift
var isAirPlayVideoActive: Bool { get }
```

```objc
@property (readonly, getter=isAirPlayVideoActive) BOOL airPlayVideoActive;
```

## See Also

### Configuring AirPlay behavior
- [var allowsAirPlayVideo: Bool](./allowsairplayvideo.md)
  A Boolean value that indicates whether the player allows AirPlay video playback.
- [var usesAirPlayVideoWhileAirPlayScreenIsActive: Bool](./usesairplayvideowhileairplayscreenisactive.md)
  A Boolean value that indicates whether the player automatically switches to AirPlay Video while AirPlay Screen is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/isairplayvideoactive)*