# AVAudioConnectionPoint

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVAudioConnectionPoint : NSObject
```

## Overview

Instances of this class are immutable.

## Topics

### Creating a connection point
- [init(node: AVAudioNode, bus: AVAudioNodeBus)](./avaudioconnectionpoint/init%28node,bus%29.md)
  Creates a connection point object.
### Getting connection point properties
- [func inputConnectionPoint(for: AVAudioNode, inputBus: AVAudioNodeBus) -> AVAudioConnectionPoint?](./avaudioengine/inputconnectionpoint%28for,inputbus%29.md)
  Returns connection information about a node’s input bus.
- [func outputConnectionPoints(for: AVAudioNode, outputBus: AVAudioNodeBus) -> [AVAudioConnectionPoint]](./avaudioengine/outputconnectionpoints%28for,outputbus%29.md)
  Returns connection information about a node’s output bus.
- [var bus: AVAudioNodeBus](./avaudioconnectionpoint/bus.md)
  The bus on the node in the connection point.
- [var node: AVAudioNode?](./avaudioconnectionpoint/node.md)
  The node in the connection point.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Using connection points
- [func connect(AVAudioNode, to: [AVAudioConnectionPoint], fromBus: AVAudioNodeBus, format: AVAudioFormat?)](./avaudioengine/connect%28_,to,frombus,format%29.md)
  Establishes a connection between a source node and multiple destination nodes.
- [func inputConnectionPoint(for: AVAudioNode, inputBus: AVAudioNodeBus) -> AVAudioConnectionPoint?](./avaudioengine/inputconnectionpoint%28for,inputbus%29.md)
  Returns connection information about a node’s input bus.
- [func outputConnectionPoints(for: AVAudioNode, outputBus: AVAudioNodeBus) -> [AVAudioConnectionPoint]](./avaudioengine/outputconnectionpoints%28for,outputbus%29.md)
  Returns connection information about a node’s output bus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconnectionpoint)*