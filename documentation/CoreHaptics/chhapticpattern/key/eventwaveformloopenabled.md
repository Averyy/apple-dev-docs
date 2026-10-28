# eventWaveformLoopEnabled

**Framework**: Core Haptics  
**Kind**: property  
**Role**: Type Property

A key for a Boolean value that indicates whether to loop custom audio events.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static let eventWaveformLoopEnabled: CHHapticPattern.Key
```

```c
extern CHHapticPatternKey CHHapticPatternKeyEventWaveformLoopEnabled;
```

## Discussion

Set a value of [`true`](../../../Swift/true.md) to indicate that events of type [`audioCustom`](../../chhapticevent/eventtype/audiocustom.md) should loop playback.

The default value is [`false`](../../../Swift/false.md).

## See Also

### Haptic Pattern Keys
- [static let event: CHHapticPattern.Key](./event.md)
  A key that identifies the beginning of a haptic event definition.
- [static let eventDuration: CHHapticPattern.Key](./eventduration.md)
  A key that identifies the duration of an event.
- [static let eventParameters: CHHapticPattern.Key](./eventparameters.md)
  A key that identifies the beginning of an array of fixed parameter definitions.
- [static let eventType: CHHapticPattern.Key](./eventtype.md)
  A key that identifies the type of event.
- [static let eventWaveformPath: CHHapticPattern.Key](./eventwaveformpath.md)
  A key that identifies the path to the local file that contains the audio waveform.
- [static let eventWaveformUseVolumeEnvelope: CHHapticPattern.Key](./eventwaveformusevolumeenvelope.md)
  A key that identifies whether audio file playback fades in and out using an envelope.
- [static let parameter: CHHapticPattern.Key](./parameter.md)
  A key that identifies the beginning of a parameter definition.
- [static let parameterCurve: CHHapticPattern.Key](./parametercurve.md)
  A key that identifies the beginning of a parameter curve definition.
- [static let parameterCurveControlPoints: CHHapticPattern.Key](./parametercurvecontrolpoints.md)
  A key that identifies the control points of a parameter curve.
- [static let parameterID: CHHapticPattern.Key](./parameterid.md)
  A key that identifies the parameter ID.
- [static let parameterValue: CHHapticPattern.Key](./parametervalue.md)
  A key that identifies the value of a parameter.
- [static let pattern: CHHapticPattern.Key](./pattern.md)
  A key that identifies the beginning of a haptic pattern definition.
- [static let time: CHHapticPattern.Key](./time.md)
  A key that identifies the relative time for an event or parameter, in seconds.
- [static let version: CHHapticPattern.Key](./version.md)
  A key that identifies rhe version number of a haptic pattern dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticpattern/key/eventwaveformloopenabled)*