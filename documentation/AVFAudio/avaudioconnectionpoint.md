# AVAudioConnectionPoint

**Framework**: AVFAudio  
**Kind**: class

A representation of either a source or destination connection point in the audio engine.

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
class AVAudioConnectionPoint
```

#### Overview

Instances of this class are immutable.

## Topics

### Creating a Connection Point
- [init(node: AVAudioNode, bus: AVAudioNodeBus)](avaudioconnectionpoint/init(node:bus:).md)
  Creates a connection point object.
### Getting Connection Point Properties
- [func inputConnectionPoint(for: AVAudioNode, inputBus: AVAudioNodeBus) -> AVAudioConnectionPoint?](avaudioengine/inputconnectionpoint(for:inputbus:).md)
  Returns connection information about a node’s input bus.
- [func outputConnectionPoints(for: AVAudioNode, outputBus: AVAudioNodeBus) -> [AVAudioConnectionPoint]](avaudioengine/outputconnectionpoints(for:outputbus:).md)
  Returns connection information about a node’s output bus.
- [var bus: AVAudioNodeBus](avaudioconnectionpoint/bus.md)
  The bus on the node in the connection point.
- [var node: AVAudioNode?](avaudioconnectionpoint/node.md)
  The node in the connection point.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func connect(AVAudioNode, to: [AVAudioConnectionPoint], fromBus: AVAudioNodeBus, format: AVAudioFormat?)](avaudioengine/connect(_:to:frombus:format:).md)
  Establishes a connection between a source node and multiple destination nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconnectionpoint)*