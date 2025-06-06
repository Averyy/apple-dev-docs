# connect(_:to:fromBus:format:)

**Framework**: AVFAudio  
**Kind**: method

Establishes a connection between a source node and multiple destination nodes.

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
func connect(_ sourceNode: AVAudioNode, to destNodes: [AVAudioConnectionPoint], fromBus sourceBus: AVAudioNodeBus, format: AVAudioFormat?)
```

#### Discussion

Connections that use this method are either one-to-one or one-to-many.

## Parameters

- `sourceNode`: The source node.
- `destNodes`: An array of   objects that specify destination nodes and busses.
- `sourceBus`: The output bus on the source node.
- `format`: If not  , the framework uses this value for the format of the source audio node’s output bus. In all cases, the framework matches the format of the destination audio node’s input bus to the source audio node’s output bus.

## See Also

- [class AVAudioConnectionPoint](avaudioconnectionpoint.md)
  A representation of either a source or destination connection point in the audio engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/connect(_:to:frombus:format:))*