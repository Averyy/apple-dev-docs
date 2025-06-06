# outputConnectionPoints(for:outputBus:)

**Framework**: AVFAudio  
**Kind**: method

Returns connection information about a node’s output bus.

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
func outputConnectionPoints(for node: AVAudioNode, outputBus bus: AVAudioNodeBus) -> [AVAudioConnectionPoint]
```

#### Return Value

An array of `AVAudioConnectionPoint` objects with connection information on the node’s output bus.

#### Discussion

Connections are always one-to-one or one-to-many. This method returns an empty array if there are no connections on the node’s specified output bus.

## Parameters

- `node`: The node with the output connections you’re querying.
- `bus`: The node’s output bus for connections you’re querying.

## See Also

- [func inputConnectionPoint(for: AVAudioNode, inputBus: AVAudioNodeBus) -> AVAudioConnectionPoint?](avaudioengine/inputconnectionpoint(for:inputbus:).md)
  Returns connection information about a node’s input bus.
- [var bus: AVAudioNodeBus](avaudioconnectionpoint/bus.md)
  The bus on the node in the connection point.
- [var node: AVAudioNode?](avaudioconnectionpoint/node.md)
  The node in the connection point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/outputconnectionpoints(for:outputbus:))*