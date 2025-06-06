# instructions

**Framework**: AVFoundation  
**Kind**: property

The video composition instructions.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var instructions: [any AVVideoCompositionInstructionProtocol] { get set }
```

#### Discussion

The array contains instances of [`AVVideoCompositionInstruction`](avvideocompositioninstruction-swift.class.md). For the first instruction in the array, `timeRange.start` must be less than or equal to the earliest time for which playback or other processing will be attempted (typically `kCMTimeZero`). For subsequent instructions, `timeRange.start` must be equal to the prior instruction’s end time. The end time of the last instruction must be greater than or equal to the latest time for which playback or other processing will be attempted (typically be the duration of the asset with which the instance of `AVVideoComposition` is associated).

## See Also

- [protocol AVVideoCompositionInstructionProtocol](avvideocompositioninstructionprotocol.md)
  A protocol that defines the interface for a video composition instruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/instructions)*