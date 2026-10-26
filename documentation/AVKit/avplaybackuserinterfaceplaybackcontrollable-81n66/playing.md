# playing

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

Indicates whether playback is active. Setting this property to YES starts playback; setting it to NO pauses it. This property reflects playback intent — it should remain YES while `isBuffering` is YES, indicating that playback should resume automatically once sufficient data is available. Must be key-value observable.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@property (nonatomic, readwrite, getter=isPlaying) BOOL playing;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-81n66/playing)*