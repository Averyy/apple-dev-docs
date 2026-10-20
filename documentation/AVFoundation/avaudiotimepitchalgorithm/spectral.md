# spectral

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A highest-quality time pitch algorithm that’s suitable for music.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
static let spectral: AVAudioTimePitchAlgorithm
```

```c
extern AVAudioTimePitchAlgorithm const AVAudioTimePitchAlgorithmSpectral;
```

#### Discussion

This is the most computationally intensive, and uses a variable rate from `1/32` to `32`.

## See Also

### Constants
- [static let timeDomain: AVAudioTimePitchAlgorithm](./timedomain.md)
  A modest quality time pitch algorithm that’s suitable for voice.
- [static let varispeed: AVAudioTimePitchAlgorithm](./varispeed.md)
  A high-quality time pitch algorithm that doesn’t perform pitch correction.
- [static let lowQualityZeroLatency: AVAudioTimePitchAlgorithm](./lowqualityzerolatency.md)
  A low-quality and very low computationally intensive pitch algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avaudiotimepitchalgorithm/spectral)*