# AudioUnitSetParameter(_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Sets the value of an audio unit parameter.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioUnitSetParameter(_ inUnit: AudioUnit, _ inID: AudioUnitParameterID, _ inScope: AudioUnitScope, _ inElement: AudioUnitElement, _ inValue: AudioUnitParameterValue, _ inBufferOffsetInFrames: UInt32) -> OSStatus
```

## Mentions

- [Migrating Your Audio Unit Host to the AUv3 API](migrating-your-audio-unit-host-to-the-auv3-api.md)

#### Return Value

A result code.

## Parameters

- `inUnit`: The audio unit that you want to set a parameter value for.
- `inID`: The audio unit parameter identifier.
- `inScope`: The audio unit scope for the parameter.
- `inElement`: The audio unit element for the parameter.
- `inValue`: The value that you want to apply to the parameter.
- `inBufferOffsetInFrames`: Set this to 0. To schedule the setting of a parameter value, use the   function.

## See Also

- [func AudioUnitGetParameter(AudioUnit, AudioUnitParameterID, AudioUnitScope, AudioUnitElement, UnsafeMutablePointer<AudioUnitParameterValue>) -> OSStatus](audiounitgetparameter(_:_:_:_:_:).md)
  Gets the value of an audio unit parameter.
- [func AudioUnitScheduleParameters(AudioUnit, UnsafePointer<AudioUnitParameterEvent>, UInt32) -> OSStatus](audiounitscheduleparameters(_:_:_:).md)
  Schedules changes to the value of an audio unit parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitsetparameter(_:_:_:_:_:_:))*