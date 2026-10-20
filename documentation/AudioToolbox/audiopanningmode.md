# AudioPanningMode

**Framework**: Audio Toolbox  
**Kind**: enum  
**Role**: Enumeration

Identifiers for audio panning algorithms.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum AudioPanningMode
```

```c
enum AudioPanningMode : UInt32;
```

## Topics

### Modes
- [AudioPanningMode.panningMode_SoundField](./audiopanningmode/panningmode_soundfield.md)
  The SoundField panning algorithm.
- [AudioPanningMode.panningMode_VectorBasedPanning](./audiopanningmode/panningmode_vectorbasedpanning.md)
  A vector-based panning algorithm.
### Initializers
- [init?(rawValue: UInt32)](./audiopanningmode/init%28rawvalue%29.md)

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
- [enum AudioBalanceFadeType](./audiobalancefadetype.md)
  Identifiers for audio balance fade types.
- [Audio Format Property Identifiers](./api-1577853-audio-format-property-identifier.md)
  Constants for use with the [`AudioFormatGetPropertyInfo(_:_:_:_:)`](./audioformatgetpropertyinfo%28_,_,_,_%29.md) and [`AudioFormatGetProperty(_:_:_:_:_:)`](./audioformatgetproperty%28_,_,_,_,_%29.md) functions.
- [Audio Codec Component Constants](./api-1494086-audio-codec-component-constants.md)
  Audio codec component types.
- [Audio Codec Manufacturer and Implementation Types](./api-1620448-audio-codec-manufacturer-and-imp.md)
  Identifiers for audio codec manufacturers and implementation types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiopanningmode)*