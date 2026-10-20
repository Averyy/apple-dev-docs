# CHHapticError.Code.invalidParameterType

**Framework**: Core Haptics  
**Kind**: case  
**Role**: Case

A pattern dictionary or parameter array contains an unknown or invalid parameter type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case invalidParameterType
```

```c
CHHapticErrorCodeInvalidParameterType
```

## See Also

### Error Codes
- [CHHapticError.Code.badEventEntry](./badevententry.md)
  An event is missing a required field.
- [CHHapticError.Code.badParameterEntry](./badparameterentry.md)
  A parameter in an event is missing a required field.
- [CHHapticError.Code.engineNotRunning](./enginenotrunning.md)
  Your app requested haptic playback when the engine wasn’t running.
- [CHHapticError.Code.engineStartTimeout](./enginestarttimeout.md)
  The haptic engine timed out while starting.
- [CHHapticError.Code.fileNotFound](./filenotfound.md)
  The system couldn’t find an audio file or haptic asset.
- [CHHapticError.Code.insufficientPower](./insufficientpower.md)
  The operation failed due to power restrictions.
- [CHHapticError.Code.invalidAudioResource](./invalidaudioresource.md)
  A pattern dictionary or an event array contain a reference to an invalid audio resource.
- [CHHapticError.Code.invalidAudioSession](./invalidaudiosession.md)
  The system invalidated the audio session associated with the haptic engine.
- [CHHapticError.Code.invalidEngineParameter](./invalidengineparameter.md)
  Your app attempted to initialize the haptic engine with an invalid configuration parameter.
- [CHHapticError.Code.invalidEventDuration](./invalideventduration.md)
  An event in the dictionary has an invalid duration.
- [CHHapticError.Code.invalidEventTime](./invalideventtime.md)
  The time of an event in the dictionary is invalid.
- [CHHapticError.Code.invalidEventType](./invalideventtype.md)
  The type of an event in the dictionary is invalid.
- [CHHapticError.Code.invalidPatternData](./invalidpatterndata.md)
  Your app passed an invalid pattern to the haptic engine or player.
- [CHHapticError.Code.invalidPatternDictionary](./invalidpatterndictionary.md)
  A pattern in the dictionary is missing a required field.
- [CHHapticError.Code.invalidPatternPlayer](./invalidpatternplayer.md)
  The current pattern player is no longer valid due to a server error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticerror/code/invalidparametertype)*