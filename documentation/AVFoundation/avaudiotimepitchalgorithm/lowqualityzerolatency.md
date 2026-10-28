# lowQualityZeroLatency

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A low-quality and very low computationally intensive pitch algorithm.

**Availability**:
- iOS 7.0+ - Deprecated in 15.0
- iPadOS 7.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 15.0
- watchOS 1.0+ - Deprecated in 8.0

> **Deprecated**: Use [`timeDomain`](./timedomain.md) instead.

## Declaration

```swift
static let lowQualityZeroLatency: AVAudioTimePitchAlgorithm
```

```c
extern AVAudioTimePitchAlgorithm const AVAudioTimePitchAlgorithmLowQualityZeroLatency;
```

## Discussion

This algorithm is suitable for brief fast-forward and rewind effects, as well as low-quality voice. The rate snaps to `{0.5, 0.666667, 0.8, 1.0, 1.25, 1.5, 2.0}`.

## See Also

### Constants
- [static let timeDomain: AVAudioTimePitchAlgorithm](./timedomain.md)
  A modest quality time pitch algorithm that’s suitable for voice.
- [static let varispeed: AVAudioTimePitchAlgorithm](./varispeed.md)
  A high-quality time pitch algorithm that doesn’t perform pitch correction.
- [static let spectral: AVAudioTimePitchAlgorithm](./spectral.md)
  A highest-quality time pitch algorithm that’s suitable for music.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avaudiotimepitchalgorithm/lowqualityzerolatency)*