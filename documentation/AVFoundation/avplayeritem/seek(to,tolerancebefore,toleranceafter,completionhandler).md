# seek(to:toleranceBefore:toleranceAfter:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Sets the current playback time within a specified time bound and invokes the specified block when the seek operation completes or is interrupted.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
nonisolated
func seek(to time: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler: (@Sendable (Bool) -> Void)? = nil)
```

```swift
nonisolated
func seek(to time: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime) async -> Bool
```

```objc
- (void) seekToTime:(CMTime) time toleranceBefore:(CMTime) toleranceBefore toleranceAfter:(CMTime) toleranceAfter completionHandler:(void (^)(BOOL finished)) completionHandler;
```

#### Discussion

Use this method to seek to a specified time for the item.

The time seeked to will be within the range `[time-toleranceBefore, time+toleranceAfter]` and may differ from `time` for efficiency.

Invoking this method with [`positiveInfinity`](../../CoreMedia/cmtime/positiveinfinity.md) for `toleranceBefore` and `toleranceAfter` is the same as invoking [`seek(to:completionHandler:)`](./seek%28to,completionhandler%29-91gnw.md) directly.

Seeking is constrained by the collection of seekable time ranges. If you seek to a time outside all of the seekable ranges, the seek will result in a current time within the seekable ranges.

## Parameters

- `time`: The time to which to seek.
- `toleranceBefore`: The temporal tolerance before `time`.

  Pass [`zero`](../../CoreMedia/cmtime/zero.md) to request sample accurate seeking (this may incur additional decoding delay).
- `toleranceAfter`: The temporal tolerance after `time`.

  Pass [`zero`](../../CoreMedia/cmtime/zero.md) to request sample accurate seeking (this may incur additional decoding delay).
- `completionHandler`: The block to invoke when the seek operation has finished.

## See Also

### Seeking through media
- [func seek(to: CMTime, completionHandler: ((Bool) -> Void)?)](./seek%28to,completionhandler%29-91gnw.md)
  Sets the current playback time to the specified time.
- [func seek(to: Date, completionHandler: ((Bool) -> Void)?) -> Bool](./seek%28to,completionhandler%29-1dibq.md)
  Sets the current playback time to the time specified by the date object.
- [func cancelPendingSeeks()](./cancelpendingseeks%28%29.md)
  Cancels any pending seek requests and invokes the corresponding completion handlers if present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/seek(to:tolerancebefore:toleranceafter:completionhandler:))*