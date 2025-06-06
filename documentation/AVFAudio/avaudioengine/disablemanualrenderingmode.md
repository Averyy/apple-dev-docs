# disableManualRenderingMode()

**Framework**: AVFAudio  
**Kind**: method

Sets the engine to render to or from an audio device.

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
func disableManualRenderingMode()
```

## See Also

- [func enableManualRenderingMode(AVAudioEngineManualRenderingMode, format: AVAudioFormat, maximumFrameCount: AVAudioFrameCount) throws](avaudioengine/enablemanualrenderingmode(_:format:maximumframecount:).md)
  Sets the engine to operate in manual rendering mode with the render format and maximum frame count you specify.
- [func renderOffline(AVAudioFrameCount, to: AVAudioPCMBuffer) throws -> AVAudioEngineManualRenderingStatus](avaudioengine/renderoffline(_:to:).md)
  Makes a render call to the engine operating in the offline manual rendering mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/disablemanualrenderingmode())*