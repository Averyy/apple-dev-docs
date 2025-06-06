# audioTimePitchAlgorithm

**Framework**: AVFoundation  
**Kind**: property

The processing algorithm used to manage audio pitch at different rates.

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
var audioTimePitchAlgorithm: AVAudioTimePitchAlgorithm { get set }
```

#### Discussion

The default value on iOS is [`lowQualityZeroLatency`](avaudiotimepitchalgorithm/lowqualityzerolatency.md); on macOS, the default is [`timeDomain`](avaudiotimepitchalgorithm/timedomain.md). The device automatically mutes audio when [`timebase`](avqueuedsamplebufferrendering/timebase.md) is not supported by [`AVAudioTimePitchAlgorithm`](avaudiotimepitchalgorithm.md). Modifying this property while [`timebase`](avqueuedsamplebufferrendering/timebase.md) is not `0.0` may cause the rate to briefly change to `0.0`.

## See Also

- [struct AVAudioTimePitchAlgorithm](avaudiotimepitchalgorithm.md)
  An algorithm used to set the audio pitch as the rate changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/audiotimepitchalgorithm)*