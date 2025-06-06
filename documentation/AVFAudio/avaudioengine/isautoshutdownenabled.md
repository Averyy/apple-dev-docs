# isAutoShutdownEnabled

**Framework**: AVFAudio  
**Kind**: property

A Boolean value that indicates whether autoshutdown is in an enabled state.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var isAutoShutdownEnabled: Bool { get set }
```

#### Discussion

If autoshutdown is in an enabled state, the engine can start and stop the audio hardware dynamically to conserve power. In watchOS, autoshutdown is always in an enabled state. For other platforms, it’s in a disabled state by default.

## See Also

- [typealias AVAudioEngineManualRenderingBlock](avaudioenginemanualrenderingblock.md)
  The type that represents a block that renders the engine when operating in manual rendering mode.
- [var manualRenderingBlock: AVAudioEngineManualRenderingBlock](avaudioengine/manualrenderingblock.md)
  The block that renders the engine when operating in manual rendering mode.
- [var manualRenderingFormat: AVAudioFormat](avaudioengine/manualrenderingformat.md)
  The render format of the engine in manual rendering mode.
- [var manualRenderingMaximumFrameCount: AVAudioFrameCount](avaudioengine/manualrenderingmaximumframecount.md)
  The maximum number of PCM sample frames the engine produces in any single render call in manual rendering mode.
- [var manualRenderingMode: AVAudioEngineManualRenderingMode](avaudioengine/manualrenderingmode.md)
  The manual rendering mode configured on the engine.
- [var manualRenderingSampleTime: AVAudioFramePosition](avaudioengine/manualrenderingsampletime.md)
  An indication of where the engine is on its render timeline in manual rendering mode.
- [var isInManualRenderingMode: Bool](avaudioengine/isinmanualrenderingmode.md)
  A Boolean value that indicates whether the engine is operating in manual rendering mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/isautoshutdownenabled)*