# name(forOutputBus:)

**Framework**: AVFAudio  
**Kind**: method

Retrieves the name of the output bus you specify.

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
func name(forOutputBus bus: AVAudioNodeBus) -> String?
```

#### Return Value

The name of the output bus.

## Parameters

- `bus`: The output bus from an audio node.

## See Also

- [func outputFormat(forBus: AVAudioNodeBus) -> AVAudioFormat](avaudionode/outputformat(forbus:).md)
  Retrieves the output format for the bus you specify.
- [var numberOfOutputs: Int](avaudionode/numberofoutputs.md)
  The number of output busses for the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionode/name(foroutputbus:))*