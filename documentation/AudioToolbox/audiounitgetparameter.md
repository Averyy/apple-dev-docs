# AudioUnitGetParameter(_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Gets the value of an audio unit parameter.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioUnitGetParameter(_ inUnit: AudioUnit, _ inID: AudioUnitParameterID, _ inScope: AudioUnitScope, _ inElement: AudioUnitElement, _ outValue: UnsafeMutablePointer<AudioUnitParameterValue>) -> OSStatus
```

## Mentions

- [Migrating Your Audio Unit Host to the AUv3 API](migrating-your-audio-unit-host-to-the-auv3-api.md)

#### Return Value

A result code.

## Parameters

- `inUnit`: The audio unit that you want to get a parameter value from.
- `inID`: The identifier for the parameter.
- `inScope`: The audio unit scope for the parameter.
- `inElement`: The audio unit element for the parameter.
- `outValue`: On success, contains the current value for the specified audio unit parameter.

## See Also

- [func AudioUnitScheduleParameters(AudioUnit, UnsafePointer<AudioUnitParameterEvent>, UInt32) -> OSStatus](audiounitscheduleparameters(_:_:_:).md)
  Schedules changes to the value of an audio unit parameter.
- [func AudioUnitSetParameter(AudioUnit, AudioUnitParameterID, AudioUnitScope, AudioUnitElement, AudioUnitParameterValue, UInt32) -> OSStatus](audiounitsetparameter(_:_:_:_:_:_:).md)
  Sets the value of an audio unit parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitgetparameter(_:_:_:_:_:))*