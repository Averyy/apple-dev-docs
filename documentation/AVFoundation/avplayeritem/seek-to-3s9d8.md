# seek(to:)

**Framework**: AVFoundation  
**Kind**: method

Sets the current playback time to the time specified by the date object.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+

## Declaration

```swift
@MainActor
func seek(to date: Date) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the playhead was moved to `date`, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

For playback content that is associated with a range of dates, this method moves the playhead to point within that range. This method will fail (return [`false`](https://developer.apple.com/documentation/swift/false)) if `date` is outside the range or if the content is not associated with a range of dates.

## Parameters

- `date`: The time to which to seek.

## See Also

- [func seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler: ((Bool) -> Void)?)](avplayeritem/seek(to:tolerancebefore:toleranceafter:completionhandler:).md)
  Sets the current playback time within a specified time bound and invokes the specified block when the seek operation completes or is interrupted.
- [func seek(to: CMTime, completionHandler: ((Bool) -> Void)?)](avplayeritem/seek(to:completionhandler:)-91gnw.md)
  Sets the current playback time to the specified time.
- [func seek(to: CMTime)](avplayeritem/seek(to:)-1dpto.md)
  Sets the current playback time to the specified time.
- [func seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime)](avplayeritem/seek(to:tolerancebefore:toleranceafter:).md)
  Sets the current playback time within a specified time bound.
- [func seek(to: Date) async -> Bool](avplayeritem/seek(to:)-5rt4x.md)
  Sets the current playback time to the time specified by the date object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/seek(to:)-3s9d8)*