# masterClock

**Framework**: AVFoundation  
**Kind**: property

The host clock for item time bases.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- watchOS 1.0+

## Declaration

```swift
nonisolated
var masterClock: CMClock? { get set }
```

#### Discussion

The default value of this property is `NULL`, which means that the host clock is the automatic choice. When non-`NULL`, this property overrides the automatic choice of host clock for item time bases. This is most useful when you’re synchronizing video-only movies with audio from another source.

> ❗ **Important**:  If you specify a host clock other than the appropriate audio device’s clock, the audio may drift out of sync.

 If you specify a host clock other than the appropriate audio device’s clock, the audio may drift out of sync.

## See Also

- [func setRate(Float, time: CMTime, atHostTime: CMTime)](avplayer/setrate(_:time:athosttime:).md)
  Synchronizes the playback rate and time of the current item with an external source.
- [func preroll(atRate: Float, completionHandler: ((Bool) -> Void)?)](avplayer/preroll(atrate:completionhandler:).md)
  Begins loading media data to prime the media pipelines for playback.
- [func cancelPendingPrerolls()](avplayer/cancelpendingprerolls.md)
  Cancels any pending preroll requests and invokes the corresponding completion handlers, if present.
- [var sourceClock: CMClock?](avplayer/sourceclock.md)
  A clock the player uses for item time bases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/masterclock)*