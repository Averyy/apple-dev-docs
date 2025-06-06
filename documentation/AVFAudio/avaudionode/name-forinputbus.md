# name(forInputBus:)

**Framework**: AVFAudio  
**Kind**: method

Gets the name of the input bus you specify.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func name(forInputBus bus: AVAudioNodeBus) -> String?
```

#### Return Value

The name of the input bus.

## Parameters

- `bus`: The input bus from an audio node.

## See Also

- [typealias AVAudioNodeBus](avaudionodebus.md)
  The index of a bus on an audio node.
- [func inputFormat(forBus: AVAudioNodeBus) -> AVAudioFormat](avaudionode/inputformat(forbus:).md)
  Gets the input format for the bus you specify.
- [var numberOfInputs: Int](avaudionode/numberofinputs.md)
  The number of input busses for the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionode/name(forinputbus:))*