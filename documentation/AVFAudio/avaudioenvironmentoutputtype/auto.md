# AVAudioEnvironmentOutputType.auto

**Framework**: AVFAudio  
**Kind**: case  
**Role**: Case

Automatically detects the playback route and picks the correct output.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
case auto
```

```c
AVAudioEnvironmentOutputTypeAuto
```

#### Discussion

When using the automatic output type, wired output defaults to [`AVAudioEnvironmentOutputType.headphones`](./headphones.md), and manual rendering with a two-channel output layout defaults to [`AVAudioEnvironmentOutputType.externalSpeakers`](./externalspeakers.md).

## See Also

### Choosing an output type
- [AVAudioEnvironmentOutputType.headphones](./headphones.md)
  Renders the audio output for headphones.
- [AVAudioEnvironmentOutputType.builtInSpeakers](./builtinspeakers.md)
  Renders the audio output for built-in speakers on the current hardware.
- [AVAudioEnvironmentOutputType.externalSpeakers](./externalspeakers.md)
  Renders the audio output for external speakers according to the audio environment node’s output channel layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentoutputtype/auto)*