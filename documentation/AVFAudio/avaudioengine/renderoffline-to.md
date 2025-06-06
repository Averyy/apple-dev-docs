# renderOffline(_:to:)

**Framework**: AVFAudio  
**Kind**: method

Makes a render call to the engine operating in the offline manual rendering mode.

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
func renderOffline(_ numberOfFrames: AVAudioFrameCount, to buffer: AVAudioPCMBuffer) throws -> AVAudioEngineManualRenderingStatus
```

#### Return Value

One of the status codes from [`AVAudioEngineManualRenderingStatus`](avaudioenginemanualrenderingstatus.md). Irrespective of the returned status code, on exit, the output buffer’s [`frameLength`](avaudiopcmbuffer/framelength.md) indicates the number of PCM samples the engine renders.

## Parameters

- `numberOfFrames`: The number of PCM sample frames to render.
- `buffer`: The PCM buffer the engine must render the audio for.

## See Also

- [func enableManualRenderingMode(AVAudioEngineManualRenderingMode, format: AVAudioFormat, maximumFrameCount: AVAudioFrameCount) throws](avaudioengine/enablemanualrenderingmode(_:format:maximumframecount:).md)
  Sets the engine to operate in manual rendering mode with the render format and maximum frame count you specify.
- [func disableManualRenderingMode()](avaudioengine/disablemanualrenderingmode.md)
  Sets the engine to render to or from an audio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/renderoffline(_:to:))*