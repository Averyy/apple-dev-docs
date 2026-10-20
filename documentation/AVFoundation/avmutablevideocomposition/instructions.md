# instructions

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The video composition instructions.

**Availability**:
- iOS 4.0+ - Deprecated in 26.0
- iPadOS 4.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.7+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Use AVVideoComposition.Configuration instead

## Declaration

```swift
var instructions: [any AVVideoCompositionInstructionProtocol] { get set }
```

```objc
@property (nonatomic, copy) NSArray<id<AVVideoCompositionInstruction>> * instructions;
```

#### Discussion

The array contains instances of [`AVVideoCompositionInstruction`](../avvideocompositioninstruction-swift.class.md). For the first instruction in the array, `timeRange.start` must be less than or equal to the earliest time for which playback or other processing will be attempted (typically `kCMTimeZero`). For subsequent instructions, `timeRange.start` must be equal to the prior instruction’s end time. The end time of the last instruction must be greater than or equal to the latest time for which playback or other processing will be attempted (typically be the duration of the asset with which the instance of `AVVideoComposition` is associated).

## See Also

### Specifying composition instructions
- [protocol AVVideoCompositionInstructionProtocol](../avvideocompositioninstructionprotocol.md)
  A protocol that defines the interface for a video composition instruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/instructions)*