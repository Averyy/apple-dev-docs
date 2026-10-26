# ready

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

Indicates whether the media source is ready to begin playback. This property should transition from NO to YES once the source has loaded enough data to start playback, and should not revert. Use `isBuffering` to track temporary stalls that may occur after this point. Must be key-value observable.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@property (nonatomic, readonly, getter=isReady) BOOL ready;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-81n66/ready)*