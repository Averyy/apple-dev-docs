# seek(to:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Requests that the player seek to a specified date, and to notify you when the seek is complete.

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
func seek(to date: Date) async -> Bool
```

#### Discussion

Use this method to seek the current player item to the specified time and be notified when the operation completes. If the seek request completes without being interrupted (either by another seek request or by any other operation), the completion handler you provide is executed with the `finished` parameter set to [`true`](https://developer.apple.com/documentation/Swift/true).

If another seek request is already in progress when you call this method, the completion handler for the in-progress seek request is executed immediately with the `finished` parameter set to [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `date`: The time to which to seek.
- `completionHandler`: The block to invoke when the seek operation has either been completed or been interrupted. The block takes one argument:

## See Also

- [func seek(to: CMTime)](avplayer/seek(to:)-87h2r.md)
  Requests that the player seek to a specified time.
- [func seek(to: CMTime, completionHandler: (Bool) -> Void)](avplayer/seek(to:completionhandler:)-75bls.md)
  Requests that the player seek to a specified time, and to notify you when the seek is complete.
- [func seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime)](avplayer/seek(to:tolerancebefore:toleranceafter:).md)
  Requests that the player seek to a specified time with the amount of accuracy specified by the time tolerance values.
- [func seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler: (Bool) -> Void)](avplayer/seek(to:tolerancebefore:toleranceafter:completionhandler:).md)
  Requests that the player seek to a specified time with the amount of accuracy specified by the time tolerance values, and to notify you when the seek is complete.
- [func seek(to: Date)](avplayer/seek(to:)-9h9qr.md)
  Requests that the player seek to a specified date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/seek(to:completionhandler:)-wr1l)*