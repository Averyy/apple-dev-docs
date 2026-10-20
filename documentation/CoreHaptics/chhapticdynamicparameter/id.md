# CHHapticDynamicParameter.ID

**Framework**: Core Haptics  
**Kind**: struct  
**Role**: Structure

The identifier that reveals the type of property associated with a dynamic parameter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct ID
```

```c
typedef NSString * CHHapticDynamicParameterID;
```

## Topics

### Haptic Dynamic Parameter IDs
- [static let hapticIntensityControl: CHHapticDynamicParameter.ID](./id/hapticintensitycontrol.md)
  A dynamic parameter to change the strength of a haptic pattern.
- [static let hapticSharpnessControl: CHHapticDynamicParameter.ID](./id/hapticsharpnesscontrol.md)
  A dynamic parameter to change the sharpness of a haptic pattern.
- [static let hapticAttackTimeControl: CHHapticDynamicParameter.ID](./id/hapticattacktimecontrol.md)
  A dynamic parameter to change the time when a haptic pattern’s intensity begins increasing.
- [static let hapticDecayTimeControl: CHHapticDynamicParameter.ID](./id/hapticdecaytimecontrol.md)
  A dynamic parameter to change the time when a haptic pattern’s intensity begins decreasing.
- [static let hapticReleaseTimeControl: CHHapticDynamicParameter.ID](./id/hapticreleasetimecontrol.md)
  A dynamic parameter to change the time at which to begin fading the haptic pattern.
### Audio Dynamic Parameter IDs
- [static let audioBrightnessControl: CHHapticDynamicParameter.ID](./id/audiobrightnesscontrol.md)
  A dynamic parameter to change the high-frequency content of an audio signal.
- [static let audioVolumeControl: CHHapticDynamicParameter.ID](./id/audiovolumecontrol.md)
  A dynamic parameter to change the volume or loudness of an audio signal.
- [static let audioPanControl: CHHapticDynamicParameter.ID](./id/audiopancontrol.md)
  A dynamic parameter to change the pan of an audio signal.
- [static let audioPitchControl: CHHapticDynamicParameter.ID](./id/audiopitchcontrol.md)
  A dynamic parameter to change the pitch of an audio signal.
- [static let audioAttackTimeControl: CHHapticDynamicParameter.ID](./id/audioattacktimecontrol.md)
  A dynamic parameter to change the time when an audio signal’s amplitude begins increasing.
- [static let audioDecayTimeControl: CHHapticDynamicParameter.ID](./id/audiodecaytimecontrol.md)
  A dynamic parameter to change the time when an audio signal’s amplitude begins decreasing.
- [static let audioReleaseTimeControl: CHHapticDynamicParameter.ID](./id/audioreleasetimecontrol.md)
  A dynamic parameter to change the time when an audio signal begins fading.
### Swift Initializers
- [init(rawValue: String)](./id/init%28rawvalue%29.md)
  Creates a dynamic property ID from its raw string value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a Dynamic Parameter
- [init(parameterID: CHHapticDynamicParameter.ID, value: Float, relativeTime: TimeInterval)](./init%28parameterid,value,relativetime%29.md)
  Creates a dynamic parameter from its ID, value, and start time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticdynamicparameter/id)*