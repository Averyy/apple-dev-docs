# completionDueDate

**Framework**: AVFoundation  
**Kind**: property

The deadline by which the coordinator expects the delegate to handle the command.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var completionDueDate: Date? { get }
```

## See Also

- [var shouldBufferInAnticipationOfPlayback: Bool](avdelegatingplaybackcoordinatorseekcommand/shouldbufferinanticipationofplayback.md)
  A Boolean value that indicates whether the player starts buffering in anticipation of a request to begin playback.
- [var anticipatedPlaybackRate: Float](avdelegatingplaybackcoordinatorseekcommand/anticipatedplaybackrate.md)
  The rate at which the coordinator expects playback to resume.
- [var itemTime: CMTime](avdelegatingplaybackcoordinatorseekcommand/itemtime.md)
  The time to seek to in the item timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorseekcommand/completionduedate)*