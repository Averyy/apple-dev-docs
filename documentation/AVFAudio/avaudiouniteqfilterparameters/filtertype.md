# filterType

**Framework**: AVFAudio  
**Kind**: property

The equalizer filter type.

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
var filterType: AVAudioUnitEQFilterType { get set }
```

#### Discussion

The default value is [`AVAudioUnitEQFilterType.parametric`](avaudiouniteqfiltertype/parametric.md).

## See Also

- [var bandwidth: Float](avaudiouniteqfilterparameters/bandwidth.md)
  The bandwidth of the equalizer filter, in octaves.
- [var bypass: Bool](avaudiouniteqfilterparameters/bypass.md)
  The bypass state of the equalizer filter band.
- [var frequency: Float](avaudiouniteqfilterparameters/frequency.md)
  The frequency of the equalizer filter, in hertz.
- [var gain: Float](avaudiouniteqfilterparameters/gain.md)
  The gain of the equalizer filter, in decibels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiouniteqfilterparameters/filtertype)*