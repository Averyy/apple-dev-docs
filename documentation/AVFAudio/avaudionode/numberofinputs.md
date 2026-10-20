# numberOfInputs

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The number of input busses for the node.

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
var numberOfInputs: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger numberOfInputs;
```

## See Also

### Inspecting input buses
- [typealias AVAudioNodeBus](../avaudionodebus.md)
  The index of a bus on an audio node.
- [func inputFormat(forBus: AVAudioNodeBus) -> AVAudioFormat](./inputformat%28forbus%29.md)
  Gets the input format for the bus you specify.
- [func name(forInputBus: AVAudioNodeBus) -> String?](./name%28forinputbus%29.md)
  Gets the name of the input bus you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionode/numberofinputs)*