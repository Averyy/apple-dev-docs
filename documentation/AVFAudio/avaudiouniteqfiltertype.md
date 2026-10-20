# AVAudioUnitEQFilterType

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Filter types available to use with the filter type property.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum AVAudioUnitEQFilterType
```

```c
enum AVAudioUnitEQFilterType : NSInteger;
```

## Topics

### Creating a filter type
- [init?(rawValue: Int)](./avaudiouniteqfiltertype/init%28rawvalue%29.md)
### Choosing a filter type
- [AVAudioUnitEQFilterType.parametric](./avaudiouniteqfiltertype/parametric.md)
  A type that represents a parametric filter that derives from a Butterworth analog prototype.
- [AVAudioUnitEQFilterType.lowPass](./avaudiouniteqfiltertype/lowpass.md)
  A type that represents a simple Butterworth second-order low-pass filter.
- [AVAudioUnitEQFilterType.highPass](./avaudiouniteqfiltertype/highpass.md)
  A type that represents a simple Butterworth second-order high-pass filter.
- [AVAudioUnitEQFilterType.resonantLowPass](./avaudiouniteqfiltertype/resonantlowpass.md)
  A type that represents a low-pass filter with resonance support using the bandwidth parameter.
- [AVAudioUnitEQFilterType.resonantHighPass](./avaudiouniteqfiltertype/resonanthighpass.md)
  A type that represents a high-pass filter with resonance support using the bandwidth parameter.
- [AVAudioUnitEQFilterType.bandPass](./avaudiouniteqfiltertype/bandpass.md)
  A type that represents a bandpass filter.
- [AVAudioUnitEQFilterType.bandStop](./avaudiouniteqfiltertype/bandstop.md)
  A type that represents a band-stop filter, also known as a notch filter.
- [AVAudioUnitEQFilterType.lowShelf](./avaudiouniteqfiltertype/lowshelf.md)
  A type that represents a low-shelf filter.
- [AVAudioUnitEQFilterType.highShelf](./avaudiouniteqfiltertype/highshelf.md)
  A type that represents a high-shelf filter.
- [AVAudioUnitEQFilterType.resonantLowShelf](./avaudiouniteqfiltertype/resonantlowshelf.md)
  A type that represents a low-shelf filter with resonance support using the bandwidth parameter.
- [AVAudioUnitEQFilterType.resonantHighShelf](./avaudiouniteqfiltertype/resonanthighshelf.md)
  A type that represents a high-shelf filter with resonance support using the bandwidth parameter.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring a filter band
- [var bandwidth: Float](./avaudiouniteqfilterparameters/bandwidth.md)
  The bandwidth of the equalizer filter, in octaves.
- [var bypass: Bool](./avaudiouniteqfilterparameters/bypass.md)
  The bypass state of the equalizer filter band.
- [var filterType: AVAudioUnitEQFilterType](./avaudiouniteqfilterparameters/filtertype.md)
  The equalizer filter type.
- [var frequency: Float](./avaudiouniteqfilterparameters/frequency.md)
  The frequency of the equalizer filter, in hertz.
- [var gain: Float](./avaudiouniteqfilterparameters/gain.md)
  The gain of the equalizer filter, in decibels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiouniteqfiltertype)*