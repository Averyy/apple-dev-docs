# isPreparedToPlay

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value indicating whether a media player is ready to play.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var isPreparedToPlay: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isPreparedToPlay;
```

#### Discussion

When set to [`true`](../../Swift/true.md), the media player is ready to begin playing the queued media items.

## See Also

### Starting and stopping playback
- [func play()](./play%28%29.md)
  Initiates playback of the current item.
- [func pause()](./pause%28%29.md)
  Pauses playback of the current item.
- [func stop()](./stop%28%29.md)
  Ends playback of the current item.
- [func prepareToPlay()](./preparetoplay%28%29.md)
  Prepares a media player for playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplayback/ispreparedtoplay)*