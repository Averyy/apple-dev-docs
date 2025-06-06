# AVAudioNodeBus

**Framework**: AVFAudio  
**Kind**: typealias

The index of a bus on an audio node.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias AVAudioNodeBus = Int
```

#### Discussion

An [`AVAudioNodeBus`](avaudionodebus.md) represents a bus as a zero-based index. [`AVAudioNode`](avaudionode.md) objects potentially have multiple input and output busses.

## See Also

- [func inputFormat(forBus: AVAudioNodeBus) -> AVAudioFormat](avaudionode/inputformat(forbus:).md)
  Gets the input format for the bus you specify.
- [func name(forInputBus: AVAudioNodeBus) -> String?](avaudionode/name(forinputbus:).md)
  Gets the name of the input bus you specify.
- [var numberOfInputs: Int](avaudionode/numberofinputs.md)
  The number of input busses for the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionodebus)*