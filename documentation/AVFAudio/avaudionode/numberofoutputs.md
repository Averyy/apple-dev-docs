# numberOfOutputs

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The number of output busses for the node.

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
var numberOfOutputs: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger numberOfOutputs;
```

## See Also

### Inspecting output buses
- [func outputFormat(forBus: AVAudioNodeBus) -> AVAudioFormat](./outputformat%28forbus%29.md)
  Retrieves the output format for the bus you specify.
- [func name(forOutputBus: AVAudioNodeBus) -> String?](./name%28foroutputbus%29.md)
  Retrieves the name of the output bus you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionode/numberofoutputs)*