# AVAudioEnvironmentOutputType.builtInSpeakers

**Framework**: AVFAudio  
**Kind**: case

Renders the audio output for built-in speakers on the current hardware.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
case builtInSpeakers
```

#### Discussion

The output isn’t suitable for playback on other hardware.

In iOS devices, the rendering can be specific to device orientation. Manual rendering modes may not provide the rendering you expect if the device orientation changes between rendering the audio and playing it back.

## See Also

- [AVAudioEnvironmentOutputType.auto](avaudioenvironmentoutputtype/auto.md)
  Automatically detects the playback route and picks the correct output.
- [AVAudioEnvironmentOutputType.headphones](avaudioenvironmentoutputtype/headphones.md)
  Renders the audio output for headphones.
- [AVAudioEnvironmentOutputType.externalSpeakers](avaudioenvironmentoutputtype/externalspeakers.md)
  Renders the audio output for external speakers according to the audio environment node’s output channel layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentoutputtype/builtinspeakers)*