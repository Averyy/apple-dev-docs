# AVAudioEngineManualRenderingBlock

**Framework**: AVFAudio  
**Kind**: typealias

The type that represents a block that renders the engine when operating in manual rendering mode.

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
typealias AVAudioEngineManualRenderingBlock = (AVAudioFrameCount, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<OSStatus>?) -> AVAudioEngineManualRenderingStatus
```

#### Return Value

One of the status codes from [`AVAudioEngineManualRenderingStatus`](avaudioenginemanualrenderingstatus.md). Irrespective of the returned status code, on exit, the output buffer’s [`frameLength`](avaudiopcmbuffer/framelength.md) indicates the number of PCM samples the engine renders.

## Parameters

- `numberOfFrames`: The number of PCM sample frames to render.
- `outBuffer`: The PCM buffer the engine must render the audio for.
- `outError`: On exit, if an error occurs during rendering, a description of the error.

## See Also

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
- [var isAutoShutdownEnabled: Bool](avaudioengine/isautoshutdownenabled.md)
  A Boolean value that indicates whether autoshutdown is in an enabled state.
- [var isInManualRenderingMode: Bool](avaudioengine/isinmanualrenderingmode.md)
  A Boolean value that indicates whether the engine is operating in manual rendering mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenginemanualrenderingblock)*