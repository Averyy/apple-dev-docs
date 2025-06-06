# pan

**Framework**: AVFAudio  
**Kind**: property  
**Required**: Yes

The bus’s stereo pan.

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
var pan: Float { get set }
```

#### Discussion

The default value is `0.0`, and the range of valid values is `-1.0` to `1.0`. Only the [`AVAudioEnvironmentNode`](avaudioenvironmentnode.md) class implements this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiostereomixing/pan)*