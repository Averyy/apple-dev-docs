# gain

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) float gain;
```

## Discussion

The default value is `0 dB`. The valid range of values is `-96 dB` through `24 dB`.

## See Also

### Configuring a filter band
- [var bandwidth: Float](./bandwidth.md)
  The bandwidth of the equalizer filter, in octaves.
- [var bypass: Bool](./bypass.md)
  The bypass state of the equalizer filter band.
- [var filterType: AVAudioUnitEQFilterType](./filtertype.md)
  The equalizer filter type.
- [enum AVAudioUnitEQFilterType](../avaudiouniteqfiltertype.md)
  Filter types available to use with the filter type property.
- [var frequency: Float](./frequency.md)
  The frequency of the equalizer filter, in hertz.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiouniteqfilterparameters/gain)*