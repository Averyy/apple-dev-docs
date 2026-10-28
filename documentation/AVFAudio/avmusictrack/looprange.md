# loopRange

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The timestamp range for the loop, in beats.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var loopRange: AVBeatRange { get set }
```

```objc
@property (nonatomic) AVBeatRange loopRange;
```

## Discussion

You set the loop by specifying its beat range.

## See Also

### Configuring the looping state
- [var isLoopingEnabled: Bool](./isloopingenabled.md)
  A Boolean value that indicates whether the track is in a looping state.
- [var numberOfLoops: Int](./numberofloops.md)
  The number of times the track’s loop repeats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictrack/looprange)*