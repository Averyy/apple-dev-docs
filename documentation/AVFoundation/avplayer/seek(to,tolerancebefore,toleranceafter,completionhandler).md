# seek(to:toleranceBefore:toleranceAfter:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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
func seek(to time: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler: @escaping @Sendable (Bool) -> Void)
```

```swift
nonisolated
func seek(to time: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime) async -> Bool
```

```objc
- (void) seekToTime:(CMTime) time toleranceBefore:(CMTime) toleranceBefore toleranceAfter:(CMTime) toleranceAfter completionHandler:(void (^)(BOOL finished)) completionHandler;
```

#### Discussion

Use this method to seek to a specified time for the current player item and to be notified when the seek operation is complete.

The time seeked to will be within the range `[time-beforeTolerance, time+afterTolerance]`, and may differ from the specified time for efficiency. You can request sample accurate seeking by passing a time value of`kCMTimeZero` for both `toleranceBefore` and `toleranceAfter`. Sample accurate seeking may incur additional decoding delay which can impact seeking performance.

Invoking this method with `toleranceBefore` set to [`positiveInfinity`](../../CoreMedia/cmtime/positiveinfinity.md) and `toleranceAfter` set to [`positiveInfinity`](../../CoreMedia/cmtime/positiveinfinity.md) is the same as invoking [`seek(to:)`](./seek%28to%29-87h2r.md).

The completion handler for any prior seek request that is still in process will be invoked immediately with the `finished` parameter set to [`false`](../../Swift/false.md). If the new request completes without being interrupted by another seek request or by any other operation the specified completion handler will be invoked with the `finished` parameter set to [`true`](../../Swift/true.md).

## Parameters

- `time`: The time to which to seek.
- `toleranceBefore`: The tolerance allowed before `time`.
- `toleranceAfter`: The tolerance allowed after `time`.
- `completionHandler`: The block to invoke when the seek operation has either been completed or been interrupted.

  The block takes one argument:

  - **finished**: Indicated whether the seek operation completed.

## See Also

### Seeking through media
- [func seek(to: CMTime)](./seek%28to%29-87h2r.md)
  Requests that the player seek to a specified time.
- [func seek(to: CMTime, completionHandler: (Bool) -> Void)](./seek%28to,completionhandler%29-75bls.md)
  Requests that the player seek to a specified time, and to notify you when the seek is complete.
- [func seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime)](./seek%28to,tolerancebefore,toleranceafter%29.md)
  Requests that the player seek to a specified time with the amount of accuracy specified by the time tolerance values.
- [func seek(to: Date)](./seek%28to%29-9h9qr.md)
  Requests that the player seek to a specified date.
- [func seek(to: Date, completionHandler: (Bool) -> Void)](./seek%28to,completionhandler%29-wr1l.md)
  Requests that the player seek to a specified date, and to notify you when the seek is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/seek(to:tolerancebefore:toleranceafter:completionhandler:))*