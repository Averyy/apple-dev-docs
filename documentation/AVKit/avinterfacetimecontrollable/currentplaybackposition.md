# currentPlaybackPosition

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The current playback position within the media time, expressed in seconds from the start of the content. This value should be within the bounds defined by the start and duration properties and represents the exact temporal position of playback. Must be key-value observable.

## Declaration

```objc
@property (nonatomic, readwrite) CMTime currentPlaybackPosition;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacetimecontrollable/currentplaybackposition)*