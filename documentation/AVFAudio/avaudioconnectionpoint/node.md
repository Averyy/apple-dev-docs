# node

**Framework**: AVFAudio  
**Kind**: property

The node in the connection point.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
weak var node: AVAudioNode? { get }
```

## See Also

- [func inputConnectionPoint(for: AVAudioNode, inputBus: AVAudioNodeBus) -> AVAudioConnectionPoint?](avaudioengine/inputconnectionpoint(for:inputbus:).md)
  Returns connection information about a node’s input bus.
- [func outputConnectionPoints(for: AVAudioNode, outputBus: AVAudioNodeBus) -> [AVAudioConnectionPoint]](avaudioengine/outputconnectionpoints(for:outputbus:).md)
  Returns connection information about a node’s output bus.
- [var bus: AVAudioNodeBus](avaudioconnectionpoint/bus.md)
  The bus on the node in the connection point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconnectionpoint/node)*