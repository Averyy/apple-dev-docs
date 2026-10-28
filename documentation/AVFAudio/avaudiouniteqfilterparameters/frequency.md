# frequency

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The frequency of the equalizer filter, in hertz.

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
var frequency: Float { get set }
```

```objc
@property (nonatomic) float frequency;
```

## Discussion

The valid range of values is `20 Hz` through `(SampleRate/2)`.

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
- [var gain: Float](./gain.md)
  The gain of the equalizer filter, in decibels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiouniteqfilterparameters/frequency)*