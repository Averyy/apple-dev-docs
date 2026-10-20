# isLoopingEnabled

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, getter=isLoopingEnabled) BOOL loopingEnabled;
```

#### Discussion

If you don’t set [`loopRange`](./looprange.md), the framework loops the full track.

## See Also

### Configuring the looping state
- [var loopRange: AVBeatRange](./looprange.md)
  The timestamp range for the loop, in beats.
- [var numberOfLoops: Int](./numberofloops.md)
  The number of times the track’s loop repeats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictrack/isloopingenabled)*