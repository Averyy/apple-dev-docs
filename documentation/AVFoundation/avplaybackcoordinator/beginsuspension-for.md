# beginSuspension(for:)

**Framework**: AVFoundation  
**Kind**: method

Tells the coordinator to stop sending playback commands temporarily when the playback object disconnects from the group activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func beginSuspension(for suspensionReason: AVCoordinatedPlaybackSuspension.Reason) -> AVCoordinatedPlaybackSuspension
```

#### Return Value

A suspension object.

#### Discussion

End a suspension by calling its [`end()`](avcoordinatedplaybacksuspension/end().md) or [`end(proposingNewTime:)`](avcoordinatedplaybacksuspension/end(proposingnewtime:).md) method.

## Parameters

- `suspensionReason`: The reason for the suspension. Indicate a system-defined value or a custom suspension reason.

## See Also

- [class AVCoordinatedPlaybackSuspension](avcoordinatedplaybacksuspension.md)
  An object that represents a temporary suspension of coordinated playback.
- [func expectedItemTime(atHostTime: CMTime) -> CMTime](avplaybackcoordinator/expecteditemtime(athosttime:).md)
  Returns a time in the current item’s timeline that the coordinator expects to play at the specified host time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplaybackcoordinator/beginsuspension(for:))*