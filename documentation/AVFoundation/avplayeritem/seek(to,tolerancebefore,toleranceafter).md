# seek(to:toleranceBefore:toleranceAfter:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Sets the current playback time within a specified time bound.

**Availability**:
- iOS 4.0+ - Deprecated in 11.0
- iPadOS 4.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.7+ - Deprecated in 10.13
- tvOS 9.0+ - Deprecated in 11.0

> **Deprecated**: Use [`seek(to:toleranceBefore:toleranceAfter:completionHandler:)`](./seek%28to,tolerancebefore,toleranceafter,completionhandler%29.md) instead.

## Declaration

```swift
func seek(to time: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime)
```

```objc
- (void) seekToTime:(CMTime) time toleranceBefore:(CMTime) toleranceBefore toleranceAfter:(CMTime) toleranceAfter;
```

#### Discussion

The time seeked to will be within the range `[time-beforeTolerance, time+afterTolerance]`, and may differ from the specified time for efficiency. If you pass `kCMTimeZero` for both `toleranceBefore` and `toleranceAfter` (to request sample accurate seeking), you may incur additional decoding delay that impacts seeking performance.

Passing `kCMTimePositiveInfinity` for both `toleranceBefore` and `toleranceAfter` is the same as messaging [`seek(to:)`](./seek%28to%29-1dpto.md) directly.

## Parameters

- `time`: The time to which you would like to move the playback cursor.
- `toleranceBefore`: The tolerance allowed before `time`.
- `toleranceAfter`: The tolerance allowed after `time`.

## See Also

### Related Documentation
- [func seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler: ((Bool) -> Void)?)](./seek%28to,tolerancebefore,toleranceafter,completionhandler%29.md)
  Sets the current playback time within a specified time bound and invokes the specified block when the seek operation completes or is interrupted.
- [func seek(to: CMTime, completionHandler: ((Bool) -> Void)?)](./seek%28to,completionhandler%29-91gnw.md)
  Sets the current playback time to the specified time.
### Seeking through media
- [func seek(to: CMTime)](./seek%28to%29-1dpto.md)
  Sets the current playback time to the specified time.
- [func seek(to: Date) async -> Bool](./seek%28to%29-5rt4x.md)
  Sets the current playback time to the time specified by the date object.
- [func seek(to: Date) -> Bool](./seek%28to%29-3s9d8.md)
  Sets the current playback time to the time specified by the date object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/seek(to:tolerancebefore:toleranceafter:))*