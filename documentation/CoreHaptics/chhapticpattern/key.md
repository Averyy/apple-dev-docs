# CHHapticPattern.Key

**Framework**: Core Haptics  
**Kind**: struct  
**Role**: Structure

Constants that define the keys you use to create a haptic pattern dictionary.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct Key
```

```c
typedef NSString * CHHapticPatternKey;
```

## Topics

### Haptic Pattern Keys
- [static let event: CHHapticPattern.Key](./key/event.md)
  A key that identifies the beginning of a haptic event definition.
- [static let eventDuration: CHHapticPattern.Key](./key/eventduration.md)
  A key that identifies the duration of an event.
- [static let eventParameters: CHHapticPattern.Key](./key/eventparameters.md)
  A key that identifies the beginning of an array of fixed parameter definitions.
- [static let eventType: CHHapticPattern.Key](./key/eventtype.md)
  A key that identifies the type of event.
- [static let eventWaveformLoopEnabled: CHHapticPattern.Key](./key/eventwaveformloopenabled.md)
  A key for a Boolean value that indicates whether to loop custom audio events.
- [static let eventWaveformPath: CHHapticPattern.Key](./key/eventwaveformpath.md)
  A key that identifies the path to the local file that contains the audio waveform.
- [static let eventWaveformUseVolumeEnvelope: CHHapticPattern.Key](./key/eventwaveformusevolumeenvelope.md)
  A key that identifies whether audio file playback fades in and out using an envelope.
- [static let parameter: CHHapticPattern.Key](./key/parameter.md)
  A key that identifies the beginning of a parameter definition.
- [static let parameterCurve: CHHapticPattern.Key](./key/parametercurve.md)
  A key that identifies the beginning of a parameter curve definition.
- [static let parameterCurveControlPoints: CHHapticPattern.Key](./key/parametercurvecontrolpoints.md)
  A key that identifies the control points of a parameter curve.
- [static let parameterID: CHHapticPattern.Key](./key/parameterid.md)
  A key that identifies the parameter ID.
- [static let parameterValue: CHHapticPattern.Key](./key/parametervalue.md)
  A key that identifies the value of a parameter.
- [static let pattern: CHHapticPattern.Key](./key/pattern.md)
  A key that identifies the beginning of a haptic pattern definition.
- [static let time: CHHapticPattern.Key](./key/time.md)
  A key that identifies the relative time for an event or parameter, in seconds.
- [static let version: CHHapticPattern.Key](./key/version.md)
  A key that identifies rhe version number of a haptic pattern dictionary.
### Initializers
- [init(rawValue: String)](./key/init%28rawvalue%29.md)
  Creates a pattern key with a string.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a Haptic Pattern
- [init(contentsOf: URL) throws](./init%28contentsof%29.md)
  Creates a haptic pattern with the contents of an AHAP file.
- [init(events: [CHHapticEvent], parameterCurves: [CHHapticParameterCurve]) throws](./init%28events,parametercurves%29.md)
  Constructs a haptic pattern from a series of events and parameter curves.
- [init(events: [CHHapticEvent], parameters: [CHHapticDynamicParameter]) throws](./init%28events,parameters%29.md)
  Constructs a haptic pattern from a series of events and parameters.
- [init(dictionary: [CHHapticPattern.Key : Any]) throws](./init%28dictionary%29.md)
  Creates a haptic pattern from a property list dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticpattern/key)*