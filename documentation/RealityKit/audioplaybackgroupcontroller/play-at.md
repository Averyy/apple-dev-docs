# play(at:)

**Framework**: RealityKit  
**Kind**: method

Plays all audio resources in the group asynchronously at a specified time.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func play(at time: AVAudioTime) throws
```

#### Discussion

Use this method to schedule playback of the group to a precise time in the future. This method enables sample-accurate timing for the group and synchronization with other audio sources.

Any call to [`play()`](audioplaybackgroupcontroller/play().md) cancels a pending scheduled time and plays audio immediately. Any call to [`play(at:)`](audioplaybackgroupcontroller/play(at:).md) cancels a pending scheduled time and reschedules to the new time. The controller ignores calls to [`play()`](audioplaybackgroupcontroller/play().md) when audio is already playing.

Audio preparation must complete before the scheduled playback time to maintain precise timing. If preparation is still in progress when the scheduled time arrives, or if the scheduled time is in the past, playback starts immediately, which may result in timing drift. For accurate synchronization, schedule a time sufficiently far in the future.

The [`isPlaying`](audioplaybackgroupcontroller/isplaying.md) property becomes `true` immediately after this call returns. Code that checks `isPlaying` to decide whether to trigger another action reads the correct state without racing against the scheduled start time.

To synchronize this group with other audio sources, use the same base time for all scheduled playback calls.

> **Note**: An error if the controller fails to schedule playback.

## Parameters

- `time`: The `AVAudioTime` at which the group should start playing.

## See Also

- [func seek(to: Duration)](audioplaybackgroupcontroller/seek(to:).md)
  Sets the playback position to the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioplaybackgroupcontroller/play(at:))*