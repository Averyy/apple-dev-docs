# timeDomain

**Framework**: AVFoundation  
**Kind**: property

A modest quality time pitch algorithm that’s suitable for voice.

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
static let timeDomain: AVAudioTimePitchAlgorithm
```

#### Discussion

This is less computationally intensive than [`spectral`](avaudiotimepitchalgorithm/spectral.md), and uses a variable rate from `1/32` to `32`.

## See Also

- [static let varispeed: AVAudioTimePitchAlgorithm](avaudiotimepitchalgorithm/varispeed.md)
  A high-quality time pitch algorithm that doesn’t perform pitch correction.
- [static let spectral: AVAudioTimePitchAlgorithm](avaudiotimepitchalgorithm/spectral.md)
  A highest-quality time pitch algorithm that’s suitable for music.
- [static let lowQualityZeroLatency: AVAudioTimePitchAlgorithm](avaudiotimepitchalgorithm/lowqualityzerolatency.md)
  A low-quality and very low computationally intensive pitch algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avaudiotimepitchalgorithm/timedomain)*