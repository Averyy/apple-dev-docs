# AudioUnitScheduleParameters(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Schedules changes to the value of an audio unit parameter.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioUnitScheduleParameters(_ inUnit: AudioUnit, _ inParameterEvent: UnsafePointer<AudioUnitParameterEvent>, _ inNumParamEvents: UInt32) -> OSStatus
```

## Mentions

- [Migrating Your Audio Unit Host to the AUv3 API](migrating-your-audio-unit-host-to-the-auv3-api.md)

#### Return Value

A result code.

#### Discussion

Use this function to schedule changes to the value of an audio unit parameter.

- A so-called  audio unit parameter event takes place at a future time and involves an immediate change from one value to another.
- A so-called  audio unit parameter event begins at a future time and proceeds linearly, over a specified number of audio samples, from a starting value to a final value.

With a single call to this function, you can schedule multiple parameter events. All the events apply only to the current audio unit render call; the events are scheduled as a part of the pre-render notification callback.

When scheduling an immediate parameter event, you provide a new value to be set at the specified sample buffer offset.

When scheduling a ramped parameter, the ramp is scheduled each audio unit render for the duration of the ramp. Each schedule of the the new audio unit render specifies the progress of the ramp.

An audio unit parameter that accepts scheduled events indicates this through its `AudioUnitParameterInfo` structure.

## Parameters

- `inUnit`: The audio unit that you want to schedule parameter changes for.
- `inParameterEvent`: One or more parameter events that you want to schedule.
- `inNumParamEvents`: The number of audio unit parameter events represented in the   parameter.

## See Also

- [func AudioUnitGetParameter(AudioUnit, AudioUnitParameterID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<AudioUnitParameterValue>) -> OSStatus](audiounitgetparameter(_:_:_:_:_:).md)
  Gets the value of an audio unit parameter.
- [func AudioUnitSetParameter(AudioUnit, AudioUnitParameterID, AudioUnitScope, AudioUnitElement, AudioUnitParameterValue, UInt32) -> OSStatus](audiounitsetparameter(_:_:_:_:_:_:).md)
  Sets the value of an audio unit parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitscheduleparameters(_:_:_:))*