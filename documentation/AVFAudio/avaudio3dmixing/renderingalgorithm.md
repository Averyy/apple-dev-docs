# renderingAlgorithm

**Framework**: AVFAudio  
**Kind**: property  
**Required**: Yes

The type of rendering algorithm the mixer uses.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var renderingAlgorithm: AVAudio3DMixingRenderingAlgorithm { get set }
```

#### Discussion

Depending on the current output format of the [`AVAudioEnvironmentNode`](avaudioenvironmentnode.md) instance, the system may only support a subset of the rendering algorithms. You can retrieve an array of valid rendering algorithms by calling the [`applicableRenderingAlgorithms`](avaudioenvironmentnode/applicablerenderingalgorithms.md) function of the [`AVAudioEnvironmentNode`](avaudioenvironmentnode.md) instance.

The default rendering algorithm is [`AVAudio3DMixingRenderingAlgorithm.equalPowerPanning`](avaudio3dmixingrenderingalgorithm/equalpowerpanning.md). Only the [`AVAudioEnvironmentNode`](avaudioenvironmentnode.md) class implements this property.

## See Also

- [enum AVAudio3DMixingRenderingAlgorithm](avaudio3dmixingrenderingalgorithm.md)
  The types of rendering algorithms available per input bus of the environment node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dmixing/renderingalgorithm)*