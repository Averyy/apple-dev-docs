# scanSpeed

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The speed multiplier used during scanning (fast-forward or rewind). This is a transient override that is active only while `state` is scanning. It does not affect `playbackSpeed`. When scanning ends, playback resumes at `playbackSpeed`. Must be key-value observable.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@property (nonatomic, readwrite) float scanSpeed;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-81n66/scanspeed)*