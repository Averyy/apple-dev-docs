# shouldBufferInAnticipationOfPlayback

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the player starts buffering in preparation for a request to begin playback.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var shouldBufferInAnticipationOfPlayback: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL shouldBufferInAnticipationOfPlayback;
```

## Discussion

A [`true`](../../Swift/true.md) value indicates that a participant player requests starting playback at the [`anticipatedPlaybackRate`](./anticipatedplaybackrate.md) value.

## See Also

### Accessing command details
- [var anticipatedPlaybackRate: Float](./anticipatedplaybackrate.md)
  The rate at which the coordinator expects the current item to play.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorpausecommand/shouldbufferinanticipationofplayback)*