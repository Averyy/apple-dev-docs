# applicableRenderingAlgorithms

**Framework**: AVFAudio  
**Kind**: property

An array of rendering algorithms applicable to the environment node.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var applicableRenderingAlgorithms: [NSNumber] { get }
```

#### Discussion

The `AVAudioEnvironmentNode` class supports several rendering algorithms for each input bus as [`AVAudio3DMixingRenderingAlgorithm`](avaudio3dmixingrenderingalgorithm.md) defines.

Depending on the current output format of the environment node, this method returns an immutable array of the applicable rendering algorithms. This subset of applicable rendering algorithms is important when you configure the environment node to a multichannel output format because only a subset of the algorithms render to all of the channels.

Retrieve the applicable algorithms after a successful connection to the destination node through one of the [`AVAudioEngine`](avaudioengine.md) connect methods.

## See Also

- [func connect(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?)](avaudioengine/connect(_:to:format:).md)
  Establishes a connection between two nodes.
- [func connect(AVAudioNode, to: AVAudioNode, fromBus: AVAudioNodeBus, toBus: AVAudioNodeBus, format: AVAudioFormat?)](avaudioengine/connect(_:to:frombus:tobus:format:).md)
  Establishes a connection between two nodes, specifying the input and output busses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentnode/applicablerenderingalgorithms)*