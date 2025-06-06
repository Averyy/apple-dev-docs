# AVAudioUnitEQFilterParameters

**Framework**: Avfaudio  
**Kind**: class

An object that encapsulates the parameters that the equalizer uses.

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
class AVAudioUnitEQFilterParameters
```

#### Overview

> **Note**:  Don’t create an instance of the `AVAudioUnitEQFilterParameters` class directly. Use the array that returns from the [`bands`](avaudiouniteq/bands.md) property of [`AVAudioUnitEQ`](avaudiouniteq.md).

## Topics

### Getting and Setting Equalizer Filter Parameters
- [var bandwidth: Float](avaudiouniteqfilterparameters/bandwidth.md)
  The bandwidth of the equalizer filter, in octaves.
- [var bypass: Bool](avaudiouniteqfilterparameters/bypass.md)
  The bypass state of the equalizer filter band.
- [var filterType: AVAudioUnitEQFilterType](avaudiouniteqfilterparameters/filtertype.md)
  The equalizer filter type.
- [var frequency: Float](avaudiouniteqfilterparameters/frequency.md)
  The frequency of the equalizer filter, in hertz.
- [var gain: Float](avaudiouniteqfilterparameters/gain.md)
  The gain of the equalizer filter, in decibels.
### Constants
- [enum AVAudioUnitEQFilterType](avaudiouniteqfiltertype.md)
  Filter types available to use with the filter type property.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var bands: [AVAudioUnitEQFilterParameters]](avaudiouniteq/bands.md)
  An array of equalizer filter parameters.
- [var globalGain: Float](avaudiouniteq/globalgain.md)
  The overall gain adjustment that the audio unit applies to the signal, in decibels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AVFAudio/avaudiouniteqfilterparameters)*