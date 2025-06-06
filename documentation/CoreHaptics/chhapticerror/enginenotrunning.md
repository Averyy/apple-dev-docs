# engineNotRunning

**Framework**: Core Haptics  
**Kind**: property

Your app requested haptic playback when the engine wasn’t running.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static var engineNotRunning: CHHapticError.Code { get }
```

## See Also

- [static var badEventEntry: CHHapticError.Code](chhapticerror/badevententry.md)
  An event is missing a required field.
- [static var badParameterEntry: CHHapticError.Code](chhapticerror/badparameterentry.md)
  A parameter in an event is missing a required field.
- [static var engineStartTimeout: CHHapticError.Code](chhapticerror/enginestarttimeout.md)
  The haptic engine timed out while starting.
- [static var fileNotFound: CHHapticError.Code](chhapticerror/filenotfound.md)
  The system couldn’t find an audio file or haptic asset.
- [static var insufficientPower: CHHapticError.Code](chhapticerror/insufficientpower.md)
  The operation failed due to power restrictions.
- [static var invalidAudioResource: CHHapticError.Code](chhapticerror/invalidaudioresource.md)
  A pattern dictionary or an event array contain a reference to an invalid audio resource.
- [static var invalidAudioSession: CHHapticError.Code](chhapticerror/invalidaudiosession.md)
  The system invalidated the audio session associated with the haptic engine.
- [static var invalidEngineParameter: CHHapticError.Code](chhapticerror/invalidengineparameter.md)
  Your app attempted to initialize the haptic engine with an invalid configuration parameter.
- [static var invalidEventDuration: CHHapticError.Code](chhapticerror/invalideventduration.md)
  An event in the dictionary has an invalid duration.
- [static var invalidEventTime: CHHapticError.Code](chhapticerror/invalideventtime.md)
  The time of an event in the dictionary is invalid.
- [static var invalidEventType: CHHapticError.Code](chhapticerror/invalideventtype.md)
  The type of an event in the dictionary is invalid.
- [static var invalidParameterType: CHHapticError.Code](chhapticerror/invalidparametertype.md)
  A pattern dictionary or parameter array contains an unknown or invalid parameter type.
- [static var invalidPatternData: CHHapticError.Code](chhapticerror/invalidpatterndata.md)
  Your app passed an invalid pattern to the haptic engine or player.
- [static var invalidPatternDictionary: CHHapticError.Code](chhapticerror/invalidpatterndictionary.md)
  A pattern in the dictionary is missing a required field.
- [static var invalidPatternPlayer: CHHapticError.Code](chhapticerror/invalidpatternplayer.md)
  The current pattern player is no longer valid due to a server error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticerror/enginenotrunning)*