# bypass

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The bypass state of the equalizer filter band.

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
var bypass: Bool { get set }
```

```objc
@property (nonatomic) BOOL bypass;
```

## Discussion

[`true`](../../Swift/true.md) if the bypass is active; otherwise, [`false`](../../Swift/false.md).

## See Also

### Configuring a filter band
- [var bandwidth: Float](./bandwidth.md)
  The bandwidth of the equalizer filter, in octaves.
- [var filterType: AVAudioUnitEQFilterType](./filtertype.md)
  The equalizer filter type.
- [enum AVAudioUnitEQFilterType](../avaudiouniteqfiltertype.md)
  Filter types available to use with the filter type property.
- [var frequency: Float](./frequency.md)
  The frequency of the equalizer filter, in hertz.
- [var gain: Float](./gain.md)
  The gain of the equalizer filter, in decibels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiouniteqfilterparameters/bypass)*