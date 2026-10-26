# ready

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

Indicates whether the media source is ready for playback operations. Returns YES when the source has sufficient data and is prepared to begin playback. Use this property to determine when playback controls should be enabled and when the media can respond to play requests. Must be key-value observable.

## Declaration

```objc
@property (nonatomic, readonly, getter=isReady) BOOL ready;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfaceplaybackcontrollable/ready)*