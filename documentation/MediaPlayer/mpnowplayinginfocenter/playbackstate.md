# playbackState

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The current playback state of the app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.12.2+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var playbackState: MPNowPlayingPlaybackState { get set }
```

```objc
@property (nonatomic) MPNowPlayingPlaybackState playbackState;
```

#### Discussion

This property only applies to macOS. You must set this property every time the app begins or halts playback, otherwise remote control functionality may not work as expected.

## See Also

### Setting the playback state in macOS
- [enum MPNowPlayingPlaybackState](../mpnowplayingplaybackstate.md)
  The playback state of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocenter/playbackstate)*