# playbackPosition

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A snapshot of the current playback position. Must be updated — with a fresh `hostTime` — on play, pause, seek, scan, and buffering state changes. Must be key-value observable.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@property (nonatomic, copy, readonly) AVPlaybackUserInterfacePlaybackPosition * playbackPosition;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacetimecontrollable-62fq2/playbackposition)*