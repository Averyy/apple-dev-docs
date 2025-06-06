# lowQualityZeroLatency

**Framework**: AVFoundation  
**Kind**: property

A low-quality and very low computationally intensive pitch algorithm.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- watchOS 1.0+

## Declaration

```swift
static let lowQualityZeroLatency: AVAudioTimePitchAlgorithm
```

#### Discussion

This algorithm is suitable for brief fast-forward and rewind effects, as well as low-quality voice. The rate snaps to `{0.5, 0.666667, 0.8, 1.0, 1.25, 1.5, 2.0}`.

## See Also

- [static let timeDomain: AVAudioTimePitchAlgorithm](avaudiotimepitchalgorithm/timedomain.md)
  A modest quality time pitch algorithm that’s suitable for voice.
- [static let varispeed: AVAudioTimePitchAlgorithm](avaudiotimepitchalgorithm/varispeed.md)
  A high-quality time pitch algorithm that doesn’t perform pitch correction.
- [static let spectral: AVAudioTimePitchAlgorithm](avaudiotimepitchalgorithm/spectral.md)
  A highest-quality time pitch algorithm that’s suitable for music.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avaudiotimepitchalgorithm/lowqualityzerolatency)*