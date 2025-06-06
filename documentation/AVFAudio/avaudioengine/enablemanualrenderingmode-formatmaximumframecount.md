# enableManualRenderingMode(_:format:maximumFrameCount:)

**Framework**: AVFAudio  
**Kind**: method

Sets the engine to operate in manual rendering mode with the render format and maximum frame count you specify.

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
func enableManualRenderingMode(_ mode: AVAudioEngineManualRenderingMode, format pcmFormat: AVAudioFormat, maximumFrameCount: AVAudioFrameCount) throws
```

#### Discussion

Use this method to configure the engine to render in response to requests from the client. You must stop the engine before calling this method. The render format must be a PCM format and match the format of the rendering buffer.

The source nodes can supply the input data in manual rendering mode. For more information, see [`AVAudioPlayerNode`](avaudioplayernode.md) and [`AVAudioInputNode`](avaudioinputnode.md).

## Parameters

- `mode`: The manual rendering mode to use.
- `pcmFormat`: The format of the output PCM audio data from the engine.
- `maximumFrameCount`: The maximum number of PCM sample frames the engine produces in a single render call.

## See Also

- [func disableManualRenderingMode()](avaudioengine/disablemanualrenderingmode.md)
  Sets the engine to render to or from an audio device.
- [func renderOffline(AVAudioFrameCount, to: AVAudioPCMBuffer) throws -> AVAudioEngineManualRenderingStatus](avaudioengine/renderoffline(_:to:).md)
  Makes a render call to the engine operating in the offline manual rendering mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/enablemanualrenderingmode(_:format:maximumframecount:))*