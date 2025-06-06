# itemTime

**Framework**: AVFoundation  
**Kind**: property

The time to seek to in the item timeline.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var itemTime: CMTime { get }
```

#### Discussion

> ❗ **Important**:  Don’t automatically resume playback after seeking to this time. The coordinator issues a new play command when all participants are ready to resume.

 Don’t automatically resume playback after seeking to this time. The coordinator issues a new play command when all participants are ready to resume.

## See Also

- [var shouldBufferInAnticipationOfPlayback: Bool](avdelegatingplaybackcoordinatorseekcommand/shouldbufferinanticipationofplayback.md)
  A Boolean value that indicates whether the player starts buffering in anticipation of a request to begin playback.
- [var anticipatedPlaybackRate: Float](avdelegatingplaybackcoordinatorseekcommand/anticipatedplaybackrate.md)
  The rate at which the coordinator expects playback to resume.
- [var completionDueDate: Date?](avdelegatingplaybackcoordinatorseekcommand/completionduedate.md)
  The deadline by which the coordinator expects the delegate to handle the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorseekcommand/itemtime)*