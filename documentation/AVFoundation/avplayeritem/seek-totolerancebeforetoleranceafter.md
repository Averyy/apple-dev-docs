# seek(to:toleranceBefore:toleranceAfter:)

**Framework**: AVFoundation  
**Kind**: method

Sets the current playback time within a specified time bound.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+

## Declaration

```swift
@MainActor
func seek(to time: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime)
```

#### Discussion

The time seeked to will be within the range `[time-beforeTolerance, time+afterTolerance]`, and may differ from the specified time for efficiency. If you pass `kCMTimeZero` for both `toleranceBefore` and `toleranceAfter` (to request sample accurate seeking), you may incur additional decoding delay that impacts seeking performance.

Passing `kCMTimePositiveInfinity` for both `toleranceBefore` and `toleranceAfter` is the same as messaging [`seek(to:)`](avplayeritem/seek(to:)-1dpto.md) directly.

## Parameters

- `time`: The time to which you would like to move the playback cursor.
- `toleranceBefore`: The tolerance allowed before  .
- `toleranceAfter`: The tolerance allowed after  .

## See Also

- [func seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler: ((Bool) -> Void)?)](avplayeritem/seek(to:tolerancebefore:toleranceafter:completionhandler:).md)
  Sets the current playback time within a specified time bound and invokes the specified block when the seek operation completes or is interrupted.
- [func seek(to: CMTime, completionHandler: ((Bool) -> Void)?)](avplayeritem/seek(to:completionhandler:)-91gnw.md)
  Sets the current playback time to the specified time.
- [func seek(to: CMTime)](avplayeritem/seek(to:)-1dpto.md)
  Sets the current playback time to the specified time.
- [func seek(to: Date) async -> Bool](avplayeritem/seek(to:)-5rt4x.md)
  Sets the current playback time to the time specified by the date object.
- [func seek(to: Date) -> Bool](avplayeritem/seek(to:)-3s9d8.md)
  Sets the current playback time to the time specified by the date object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/seek(to:tolerancebefore:toleranceafter:))*