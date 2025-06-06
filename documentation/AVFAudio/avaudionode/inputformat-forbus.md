# inputFormat(forBus:)

**Framework**: AVFAudio  
**Kind**: method

Gets the input format for the bus you specify.

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
func inputFormat(forBus bus: AVAudioNodeBus) -> AVAudioFormat
```

#### Return Value

An [`AVAudioFormat`](avaudioformat.md) instance that represents the input format of the bus.

## Parameters

- `bus`: An audio node bus.

## See Also

- [AVFoundation Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/AVFoundationPG/Articles/00_Introduction.html#//apple_ref/doc/uid/TP40010188)
- [typealias AVAudioNodeBus](avaudionodebus.md)
  The index of a bus on an audio node.
- [func name(forInputBus: AVAudioNodeBus) -> String?](avaudionode/name(forinputbus:).md)
  Gets the name of the input bus you specify.
- [var numberOfInputs: Int](avaudionode/numberofinputs.md)
  The number of input busses for the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionode/inputformat(forbus:))*