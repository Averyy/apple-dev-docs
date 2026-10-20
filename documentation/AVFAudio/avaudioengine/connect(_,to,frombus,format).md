# connect(_:to:fromBus:format:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Establishes a connection between a source node and multiple destination nodes.

**Availability**:
- iOS 9.0+ - Deprecated in 27.0
- iPadOS 9.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.11+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 2.0+ - Deprecated in 27.0

## Declaration

```swift
func connect(_ sourceNode: AVAudioNode, to destNodes: [AVAudioConnectionPoint], fromBus sourceBus: AVAudioNodeBus, format: AVAudioFormat?)
```

```objc
- (void) connect:(AVAudioNode *) sourceNode toConnectionPoints:(NSArray<AVAudioConnectionPoint *> *) destNodes fromBus:(AVAudioNodeBus) sourceBus format:(AVAudioFormat *) format;
```

#### Discussion

Connections that use this method are either one-to-one or one-to-many.

## Parameters

- `sourceNode`: The source node.
- `destNodes`: An array of [`AVAudioConnectionPoint`](../avaudioconnectionpoint.md) objects that specify destination nodes and busses.
- `sourceBus`: The output bus on the source node.
- `format`: If not `NULL`, the framework uses this value for the format of the source audio node’s output bus. In all cases, the framework matches the format of the destination audio node’s input bus to the source audio node’s output bus.

## See Also

### Using connection points
- [class AVAudioConnectionPoint](../avaudioconnectionpoint.md)
  A representation of either a source or destination connection point in the audio engine.
- [func inputConnectionPoint(for: AVAudioNode, inputBus: AVAudioNodeBus) -> AVAudioConnectionPoint?](./inputconnectionpoint%28for,inputbus%29.md)
  Returns connection information about a node’s input bus.
- [func outputConnectionPoints(for: AVAudioNode, outputBus: AVAudioNodeBus) -> [AVAudioConnectionPoint]](./outputconnectionpoints%28for,outputbus%29.md)
  Returns connection information about a node’s output bus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/connect(_:to:frombus:format:))*