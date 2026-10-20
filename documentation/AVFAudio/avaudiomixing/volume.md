# volume

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The bus’s input volume.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var volume: Float { get set }
```

```objc
@property (nonatomic) float volume;
```

#### Discussion

The default value is `1.0`, and the range of valid values is `0.0` to `1.0`. Only the [`AVAudioEnvironmentNode`](../avaudioenvironmentnode.md) and the [`AVAudioMixerNode`](../avaudiomixernode.md) implement this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiomixing/volume)*