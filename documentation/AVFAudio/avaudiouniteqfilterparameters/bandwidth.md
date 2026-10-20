# bandwidth

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The bandwidth of the equalizer filter, in octaves.

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
var bandwidth: Float { get set }
```

```objc
@property (nonatomic) float bandwidth;
```

#### Discussion

The value range of values is `0.05` to `5.0` octaves.

## See Also

### Configuring a filter band
- [var bypass: Bool](./bypass.md)
  The bypass state of the equalizer filter band.
- [var filterType: AVAudioUnitEQFilterType](./filtertype.md)
  The equalizer filter type.
- [enum AVAudioUnitEQFilterType](../avaudiouniteqfiltertype.md)
  Filter types available to use with the filter type property.
- [var frequency: Float](./frequency.md)
  The frequency of the equalizer filter, in hertz.
- [var gain: Float](./gain.md)
  The gain of the equalizer filter, in decibels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiouniteqfilterparameters/bandwidth)*