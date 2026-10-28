# AudioBalanceFadeType

**Framework**: Audio Toolbox  
**Kind**: enum  
**Role**: Enumeration

Identifiers for audio balance fade types.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum AudioBalanceFadeType
```

```c
enum AudioBalanceFadeType : UInt32;
```

## Overview

These constants are used as values for the `mType` field of the [`AudioBalanceFade`](./audiobalancefade.md) structure.

## Topics

### Types
- [AudioBalanceFadeType.equalPower](./audiobalancefadetype/equalpower.md)
  Overall loudness remains constant, but gain can exceed 1.0. The gain value is 1.0 when the balance and fade are in the center. From there they can increase to +3dB (1.414) and decrease to silence.
- [AudioBalanceFadeType.maxUnityGain](./audiobalancefadetype/maxunitygain.md)
  Ensures that the overall gain value never exceeds 1.0 by fading one channel as the other channel’s level rises. This can reduce overall loudness when the balance or fade is not in the center.
### Initializers
- [init?(rawValue: UInt32)](./audiobalancefadetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [Audio Format Property Identifiers](./api-1577853-audio-format-property-identifier.md)
  Constants for use with the [`AudioFormatGetPropertyInfo(_:_:_:_:)`](./audioformatgetpropertyinfo%28_,_,_,_%29.md) and [`AudioFormatGetProperty(_:_:_:_:_:)`](./audioformatgetproperty%28_,_,_,_,_%29.md) functions.
- [Audio Codec Component Constants](./api-1494086-audio-codec-component-constants.md)
  Audio codec component types.
- [Audio Codec Manufacturer and Implementation Types](./api-1620448-audio-codec-manufacturer-and-imp.md)
  Identifiers for audio codec manufacturers and implementation types.
- [enum AudioPanningMode](./audiopanningmode.md)
  Identifiers for audio panning algorithms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiobalancefadetype)*