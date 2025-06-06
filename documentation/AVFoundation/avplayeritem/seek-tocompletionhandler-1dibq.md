# seek(to:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Sets the current playback time to the time specified by the date object.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
nonisolated
func seek(to date: Date, completionHandler: ((Bool) -> Void)? = nil) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the playhead moved to the specified date or [`false`](https://developer.apple.com/documentation/swift/false) if it did not.

#### Discussion

Use this method to seek to a specified time in the player item and be notified when the operation completes. If the seek request completes without being interrupted (either by another seek request or by any other operation), the completion handler you provide is executed with the `finished` parameter set to [`true`](https://developer.apple.com/documentation/swift/true).

If another seek request is already in progress when you call this method, the completion handler for the in-progress seek request is executed immediately with the `finished` parameter set to [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `date`: The time to which to seek.
- `completionHandler`: The block to invoke when the seek operation has either been completed or been interrupted. The block takes one argument:

## See Also

- [func seek(to: CMTime, completionHandler: ((Bool) -> Void)?)](avplayeritem/seek(to:completionhandler:)-91gnw.md)
  Sets the current playback time to the specified time.
- [func seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler: ((Bool) -> Void)?)](avplayeritem/seek(to:tolerancebefore:toleranceafter:completionhandler:).md)
  Sets the current playback time within a specified time bound and invokes the specified block when the seek operation completes or is interrupted.
- [func cancelPendingSeeks()](avplayeritem/cancelpendingseeks.md)
  Cancels any pending seek requests and invokes the corresponding completion handlers if present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/seek(to:completionhandler:)-1dibq)*