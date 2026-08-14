# cancelPendingSeeks()

**Framework**: AVFoundation  
**Kind**: method

Cancels any pending seek requests and invokes the corresponding completion handlers if present.

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
func cancelPendingSeeks()
```

#### Discussion

Use this method to cancel and release the completion handlers of pending seeks.

The `finished` parameter of the completion handlers will be set to [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func seek(to: CMTime, completionHandler: ((Bool) -> Void)?)](avplayeritem/seek(to:completionhandler:)-91gnw.md)
  Sets the current playback time to the specified time.
- [func seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler: ((Bool) -> Void)?)](avplayeritem/seek(to:tolerancebefore:toleranceafter:completionhandler:).md)
  Sets the current playback time within a specified time bound and invokes the specified block when the seek operation completes or is interrupted.
- [func seek(to: Date, completionHandler: ((Bool) -> Void)?) -> Bool](avplayeritem/seek(to:completionhandler:)-1dibq.md)
  Sets the current playback time to the time specified by the date object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/cancelpendingseeks())*