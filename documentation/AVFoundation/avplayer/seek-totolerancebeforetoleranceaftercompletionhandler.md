# seek(to:toleranceBefore:toleranceAfter:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Requests that the player seek to a specified time with the amount of accuracy specified by the time tolerance values, and to notify you when the seek is complete.

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

Use this method to seek to a specified time for the current player item and to be notified when the seek operation is complete.

The time seeked to will be within the range `[time-beforeTolerance, time+afterTolerance]`, and may differ from the specified time for efficiency. You can request sample accurate seeking by passing a time value of`kCMTimeZero` for both `toleranceBefore` and `toleranceAfter`. Sample accurate seeking may incur additional decoding delay which can impact seeking performance.

Invoking this method with `toleranceBefore` set to [`positiveInfinity`](https://developer.apple.com/documentation/coremedia/cmtime/1400789-positiveinfinity) and `toleranceAfter` set to [`positiveInfinity`](https://developer.apple.com/documentation/coremedia/cmtime/1400789-positiveinfinity) is the same as invoking [`seek(to:)`](avplayer/seek(to:)-87h2r.md).

The completion handler for any prior seek request that is still in process will be invoked immediately with the `finished` parameter set to [`false`](https://developer.apple.com/documentation/swift/false). If the new request completes without being interrupted by another seek request or by any other operation the specified completion handler will be invoked with the `finished` parameter set to [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `time`: The time to which to seek.
- `toleranceBefore`: The tolerance allowed before  .
- `toleranceAfter`: The tolerance allowed after  .
- `completionHandler`: The block takes one argument:

## See Also

- [func seek(to: CMTime)](avplayer/seek(to:)-87h2r.md)
  Requests that the player seek to a specified time.
- [func seek(to: CMTime, completionHandler: (Bool) -> Void)](avplayer/seek(to:completionhandler:)-75bls.md)
  Requests that the player seek to a specified time, and to notify you when the seek is complete.
- [func seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime)](avplayer/seek(to:tolerancebefore:toleranceafter:).md)
  Requests that the player seek to a specified time with the amount of accuracy specified by the time tolerance values.
- [func seek(to: Date)](avplayer/seek(to:)-9h9qr.md)
  Requests that the player seek to a specified date.
- [func seek(to: Date, completionHandler: (Bool) -> Void)](avplayer/seek(to:completionhandler:)-wr1l.md)
  Requests that the player seek to a specified date, and to notify you when the seek is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/seek(to:tolerancebefore:toleranceafter:completionhandler:))*