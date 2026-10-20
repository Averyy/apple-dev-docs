# outputFormat(forBus:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (AVAudioFormat *) outputFormatForBus:(AVAudioNodeBus) bus;
```

#### Return Value

An [`AVAudioFormat`](../avaudioformat.md) instance that represents the output format of the bus.

## Parameters

- `bus`: An audio node bus.

## See Also

### Inspecting output buses
- [func name(forOutputBus: AVAudioNodeBus) -> String?](./name%28foroutputbus%29.md)
  Retrieves the name of the output bus you specify.
- [var numberOfOutputs: Int](./numberofoutputs.md)
  The number of output busses for the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionode/outputformat(forbus:))*