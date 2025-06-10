# seek(to:toleranceBefore:toleranceAfter:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

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
func seek(to time: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime) async -> Bool
```

#### Discussion

Use this method to seek to a specified time for the item.

The time seeked to will be within the range `[time-toleranceBefore, time+toleranceAfter]` and may differ from `time` for efficiency.

Invoking this method with [`positiveInfinity`](https://developer.apple.com/documentation/CoreMedia/CMTime/positiveInfinity) for `toleranceBefore` and `toleranceAfter` is the same as invoking [`seek(to:completionHandler:)`](avplayeritem/seek(to:completionhandler:)-91gnw.md) directly.

Seeking is constrained by the collection of seekable time ranges. If you seek to a time outside all of the seekable ranges, the seek will result in a current time within the seekable ranges.

## Parameters

- `time`: The time to which to seek.
- `toleranceBefore`: Pass   to request sample accurate seeking (this may incur additional decoding delay).
- `toleranceAfter`: Pass   to request sample accurate seeking (this may incur additional decoding delay).
- `completionHandler`: The block to invoke when the seek operation has finished.

## See Also

- [func seek(to: CMTime, completionHandler: ((Bool) -> Void)?)](avplayeritem/seek(to:completionhandler:)-91gnw.md)
  Sets the current playback time to the specified time.
- [func seek(to: Date, completionHandler: ((Bool) -> Void)?) -> Bool](avplayeritem/seek(to:completionhandler:)-1dibq.md)
  Sets the current playback time to the time specified by the date object.
- [func cancelPendingSeeks()](avplayeritem/cancelpendingseeks.md)
  Cancels any pending seek requests and invokes the corresponding completion handlers if present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/seek(to:tolerancebefore:toleranceafter:completionhandler:))*