# AVAudioUnitEQFilterType.resonantHighPass

**Framework**: AVFAudio  
**Kind**: case  
**Role**: Case

A type that represents a high-pass filter with resonance support using the bandwidth parameter.

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
case resonantHighPass
```

```c
AVAudioUnitEQFilterTypeResonantHighPass
```

#### Discussion

The necessary parameters for this type are [`frequency`](../avaudiouniteqfilterparameters/frequency.md) (`-3 dB` cutoff at specified frequency) and [`bandwidth`](../avaudiouniteqfilterparameters/bandwidth.md).

## See Also

### Choosing a filter type
- [AVAudioUnitEQFilterType.parametric](./parametric.md)
  A type that represents a parametric filter that derives from a Butterworth analog prototype.
- [AVAudioUnitEQFilterType.lowPass](./lowpass.md)
  A type that represents a simple Butterworth second-order low-pass filter.
- [AVAudioUnitEQFilterType.highPass](./highpass.md)
  A type that represents a simple Butterworth second-order high-pass filter.
- [AVAudioUnitEQFilterType.resonantLowPass](./resonantlowpass.md)
  A type that represents a low-pass filter with resonance support using the bandwidth parameter.
- [AVAudioUnitEQFilterType.bandPass](./bandpass.md)
  A type that represents a bandpass filter.
- [AVAudioUnitEQFilterType.bandStop](./bandstop.md)
  A type that represents a band-stop filter, also known as a notch filter.
- [AVAudioUnitEQFilterType.lowShelf](./lowshelf.md)
  A type that represents a low-shelf filter.
- [AVAudioUnitEQFilterType.highShelf](./highshelf.md)
  A type that represents a high-shelf filter.
- [AVAudioUnitEQFilterType.resonantLowShelf](./resonantlowshelf.md)
  A type that represents a low-shelf filter with resonance support using the bandwidth parameter.
- [AVAudioUnitEQFilterType.resonantHighShelf](./resonanthighshelf.md)
  A type that represents a high-shelf filter with resonance support using the bandwidth parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiouniteqfiltertype/resonanthighpass)*