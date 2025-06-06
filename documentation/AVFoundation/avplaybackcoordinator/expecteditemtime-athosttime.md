# expectedItemTime(atHostTime:)

**Framework**: AVFoundation  
**Kind**: method

Returns a time in the current item’s timeline that the coordinator expects to play at the specified host time.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func expectedItemTime(atHostTime hostClockTime: CMTime) -> CMTime
```

#### Return Value

A time in the current item’s timeline.

## Parameters

- `hostClockTime`: The host time to return a player item time for.

## See Also

- [func beginSuspension(for: AVCoordinatedPlaybackSuspension.Reason) -> AVCoordinatedPlaybackSuspension](avplaybackcoordinator/beginsuspension(for:).md)
  Tells the coordinator to stop sending playback commands temporarily when the playback object disconnects from the group activity.
- [class AVCoordinatedPlaybackSuspension](avcoordinatedplaybacksuspension.md)
  An object that represents a temporary suspension of coordinated playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplaybackcoordinator/expecteditemtime(athosttime:))*