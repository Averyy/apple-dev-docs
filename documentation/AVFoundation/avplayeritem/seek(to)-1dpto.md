# seek(to:)

**Framework**: AVFoundation  
**Kind**: method

Sets the current playback time to the specified time.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+

## Declaration

```swift
@MainActor
func seek(to time: CMTime)
```

#### Discussion

The time seeked to may differ from the specified time for efficiency. For sample accurate seeking see [`seek(to:toleranceBefore:toleranceAfter:)`](avplayeritem/seek(to:tolerancebefore:toleranceafter:).md).

## Parameters

- `time`: The time to which to seek.

## See Also

- [func seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler: ((Bool) -> Void)?)](avplayeritem/seek(to:tolerancebefore:toleranceafter:completionhandler:).md)
  Sets the current playback time within a specified time bound and invokes the specified block when the seek operation completes or is interrupted.
- [func seek(to: CMTime, completionHandler: ((Bool) -> Void)?)](avplayeritem/seek(to:completionhandler:)-91gnw.md)
  Sets the current playback time to the specified time.
- [func seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime)](avplayeritem/seek(to:tolerancebefore:toleranceafter:).md)
  Sets the current playback time within a specified time bound.
- [func seek(to: Date) async -> Bool](avplayeritem/seek(to:)-5rt4x.md)
  Sets the current playback time to the time specified by the date object.
- [func seek(to: Date) -> Bool](avplayeritem/seek(to:)-3s9d8.md)
  Sets the current playback time to the time specified by the date object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/seek(to:)-1dpto)*