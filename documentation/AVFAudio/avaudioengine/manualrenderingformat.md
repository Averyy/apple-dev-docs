# manualRenderingFormat

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The render format of the engine in manual rendering mode.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var manualRenderingFormat: AVAudioFormat { get }
```

```objc
@property (nonatomic, readonly) AVAudioFormat * manualRenderingFormat;
```

## See Also

### Getting manual rendering properties
- [typealias AVAudioEngineManualRenderingBlock](../avaudioenginemanualrenderingblock.md)
  The type that represents a block that renders the engine when operating in manual rendering mode.
- [var manualRenderingBlock: AVAudioEngineManualRenderingBlock](./manualrenderingblock.md)
  The block that renders the engine when operating in manual rendering mode.
- [var manualRenderingMaximumFrameCount: AVAudioFrameCount](./manualrenderingmaximumframecount.md)
  The maximum number of PCM sample frames the engine produces in any single render call in manual rendering mode.
- [var manualRenderingMode: AVAudioEngineManualRenderingMode](./manualrenderingmode.md)
  The manual rendering mode configured on the engine.
- [var manualRenderingSampleTime: AVAudioFramePosition](./manualrenderingsampletime.md)
  An indication of where the engine is on its render timeline in manual rendering mode.
- [var isAutoShutdownEnabled: Bool](./isautoshutdownenabled.md)
  A Boolean value that indicates whether autoshutdown is in an enabled state.
- [var isInManualRenderingMode: Bool](./isinmanualrenderingmode.md)
  A Boolean value that indicates whether the engine is operating in manual rendering mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/manualrenderingformat)*