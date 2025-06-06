# numberOfLoops

**Framework**: AVFAudio  
**Kind**: property

The number of times the track’s loop repeats.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var numberOfLoops: Int { get set }
```

#### Discussion

Use the value [`AVMusicTrackLoopCount.forever`](avmusictrackloopcount/forever.md) to loop the track forever. Otherwise, valid values start at `1`.

## See Also

- [var isLoopingEnabled: Bool](avmusictrack/isloopingenabled.md)
  A Boolean value that indicates whether the track is in a looping state.
- [var loopRange: AVBeatRange](avmusictrack/looprange.md)
  The timestamp range for the loop, in beats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictrack/numberofloops)*