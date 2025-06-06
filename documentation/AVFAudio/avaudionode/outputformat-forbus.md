# outputFormat(forBus:)

**Framework**: AVFAudio  
**Kind**: method

Retrieves the output format for the bus you specify.

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
func outputFormat(forBus bus: AVAudioNodeBus) -> AVAudioFormat
```

#### Return Value

An [`AVAudioFormat`](avaudioformat.md) instance that represents the output format of the bus.

## Parameters

- `bus`: An audio node bus.

## See Also

- [func name(forOutputBus: AVAudioNodeBus) -> String?](avaudionode/name(foroutputbus:).md)
  Retrieves the name of the output bus you specify.
- [var numberOfOutputs: Int](avaudionode/numberofoutputs.md)
  The number of output busses for the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionode/outputformat(forbus:))*