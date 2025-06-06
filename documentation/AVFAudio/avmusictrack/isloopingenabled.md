# isLoopingEnabled

**Framework**: AVFAudio  
**Kind**: property

A Boolean value that indicates whether the track is in a looping state.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isLoopingEnabled: Bool { get set }
```

#### Discussion

If you don’t set [`loopRange`](avmusictrack/looprange.md), the framework loops the full track.

## See Also

- [var loopRange: AVBeatRange](avmusictrack/looprange.md)
  The timestamp range for the loop, in beats.
- [var numberOfLoops: Int](avmusictrack/numberofloops.md)
  The number of times the track’s loop repeats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictrack/isloopingenabled)*