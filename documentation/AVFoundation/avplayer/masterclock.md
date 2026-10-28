# masterClock

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The host clock for item time bases.

**Availability**:
- iOS 6.0+ - Deprecated in 18.0
- iPadOS 6.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.8+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0
- watchOS 1.0+ - Deprecated in 11.0

> **Deprecated**: Use [`sourceClock`](./sourceclock.md) instead.

## Declaration

```swift
nonisolated
var masterClock: CMClock? { get set }
```

```objc
@property (nonatomic, retain, nullable) CMClockRef masterClock;
```

## Discussion

The default value of this property is `NULL`, which means that the host clock is the automatic choice. When non-`NULL`, this property overrides the automatic choice of host clock for item time bases. This is most useful when you’re synchronizing video-only movies with audio from another source.

> ❗ **Important**:  If you specify a host clock other than the appropriate audio device’s clock, the audio may drift out of sync.

## See Also

### Synchronizing multiple players
- [func setRate(Float, time: CMTime, atHostTime: CMTime)](./setrate%28_,time,athosttime%29.md)
  Synchronizes the playback rate and time of the current item with an external source.
- [func preroll(atRate: Float, completionHandler: ((Bool) -> Void)?)](./preroll%28atrate,completionhandler%29.md)
  Begins loading media data to prime the media pipelines for playback.
- [func cancelPendingPrerolls()](./cancelpendingprerolls%28%29.md)
  Cancels any pending preroll requests and invokes the corresponding completion handlers, if present.
- [var sourceClock: CMClock?](./sourceclock.md)
  A clock the player uses for item time bases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/masterclock)*