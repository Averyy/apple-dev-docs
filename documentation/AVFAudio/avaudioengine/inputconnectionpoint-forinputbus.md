# inputConnectionPoint(for:inputBus:)

**Framework**: AVFAudio  
**Kind**: method

Returns connection information about a node’s input bus.

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
func inputConnectionPoint(for node: AVAudioNode, inputBus bus: AVAudioNodeBus) -> AVAudioConnectionPoint?
```

#### Return Value

An `AVAudioConnectionPoint` object with connection information on the node’s input bus.

#### Discussion

Connections are always one-to-one or one-to-many. This method returns `nil` if there’s no connection on the node’s specified input bus.

## Parameters

- `node`: The node with the input connection you’re querying.
- `bus`: The node’s input bus for the connection you’re querying.

## See Also

- [class AVAudioConnectionPoint](avaudioconnectionpoint.md)
  A representation of either a source or destination connection point in the audio engine.
- [func connect(AVAudioNode, to: [AVAudioConnectionPoint], fromBus: AVAudioNodeBus, format: AVAudioFormat?)](avaudioengine/connect(_:to:frombus:format:).md)
  Establishes a connection between a source node and multiple destination nodes.
- [func outputConnectionPoints(for: AVAudioNode, outputBus: AVAudioNodeBus) -> [AVAudioConnectionPoint]](avaudioengine/outputconnectionpoints(for:outputbus:).md)
  Returns connection information about a node’s output bus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/inputconnectionpoint(for:inputbus:))*