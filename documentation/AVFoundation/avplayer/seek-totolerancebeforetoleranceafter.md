# seek(to:toleranceBefore:toleranceAfter:)

**Framework**: AVFoundation  
**Kind**: method

Requests that the player seek to a specified time with the amount of accuracy specified by the time tolerance values.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
nonisolated
func seek(to time: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime)
```

## Mentions

- [Controlling the transport behavior of a player](controlling-the-transport-behavior-of-a-player.md)

#### Discussion

The player seeks within the range `[time-beforeTolerance, time+afterTolerance]`, and may differ from the specified time for efficiency. You can request sample accurate seeking by passing a time value of`kCMTimeZero` for both `toleranceBefore` and `toleranceAfter`. Sample accurate seeking may incur additional decoding delay which can impact seeking performance.

Passing `kCMTimePositiveInfinity` for both `toleranceBefore` and `toleranceAfter` is the same as messaging [`seek(to:)`](avplayer/seek(to:)-87h2r.md) directly.

## Parameters

- `time`: A time to seek to.
- `toleranceBefore`: A tolerance before the target time to allow.
- `toleranceAfter`: A tolerance after the target time to allow.

## See Also

- [func seek(to: CMTime)](avplayer/seek(to:)-87h2r.md)
  Requests that the player seek to a specified time.
- [func seek(to: CMTime, completionHandler: (Bool) -> Void)](avplayer/seek(to:completionhandler:)-75bls.md)
  Requests that the player seek to a specified time, and to notify you when the seek is complete.
- [func seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler: (Bool) -> Void)](avplayer/seek(to:tolerancebefore:toleranceafter:completionhandler:).md)
  Requests that the player seek to a specified time with the amount of accuracy specified by the time tolerance values, and to notify you when the seek is complete.
- [func seek(to: Date)](avplayer/seek(to:)-9h9qr.md)
  Requests that the player seek to a specified date.
- [func seek(to: Date, completionHandler: (Bool) -> Void)](avplayer/seek(to:completionhandler:)-wr1l.md)
  Requests that the player seek to a specified date, and to notify you when the seek is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/seek(to:tolerancebefore:toleranceafter:))*