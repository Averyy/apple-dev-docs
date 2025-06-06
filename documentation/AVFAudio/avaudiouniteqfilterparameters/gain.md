# gain

**Framework**: AVFAudio  
**Kind**: property

The gain of the equalizer filter, in decibels.

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
var gain: Float { get set }
```

#### Discussion

The default value is `0 dB`. The valid range of values is `-96 dB` through `24 dB`.

## See Also

- [var bandwidth: Float](avaudiouniteqfilterparameters/bandwidth.md)
  The bandwidth of the equalizer filter, in octaves.
- [var bypass: Bool](avaudiouniteqfilterparameters/bypass.md)
  The bypass state of the equalizer filter band.
- [var filterType: AVAudioUnitEQFilterType](avaudiouniteqfilterparameters/filtertype.md)
  The equalizer filter type.
- [var frequency: Float](avaudiouniteqfilterparameters/frequency.md)
  The frequency of the equalizer filter, in hertz.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiouniteqfilterparameters/gain)*