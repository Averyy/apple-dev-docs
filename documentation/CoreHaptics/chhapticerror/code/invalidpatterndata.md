# CHHapticError.Code.invalidPatternData

**Framework**: Core Haptics  
**Kind**: case

Your app passed an invalid pattern to the haptic engine or player.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case invalidPatternData
```

## See Also

- [CHHapticError.Code.badEventEntry](chhapticerror/code/badevententry.md)
  An event is missing a required field.
- [CHHapticError.Code.badParameterEntry](chhapticerror/code/badparameterentry.md)
  A parameter in an event is missing a required field.
- [CHHapticError.Code.engineNotRunning](chhapticerror/code/enginenotrunning.md)
  Your app requested haptic playback when the engine wasn’t running.
- [CHHapticError.Code.engineStartTimeout](chhapticerror/code/enginestarttimeout.md)
  The haptic engine timed out while starting.
- [CHHapticError.Code.fileNotFound](chhapticerror/code/filenotfound.md)
  The system couldn’t find an audio file or haptic asset.
- [CHHapticError.Code.insufficientPower](chhapticerror/code/insufficientpower.md)
  The operation failed due to power restrictions.
- [CHHapticError.Code.invalidAudioResource](chhapticerror/code/invalidaudioresource.md)
  A pattern dictionary or an event array contain a reference to an invalid audio resource.
- [CHHapticError.Code.invalidAudioSession](chhapticerror/code/invalidaudiosession.md)
  The system invalidated the audio session associated with the haptic engine.
- [CHHapticError.Code.invalidEngineParameter](chhapticerror/code/invalidengineparameter.md)
  Your app attempted to initialize the haptic engine with an invalid configuration parameter.
- [CHHapticError.Code.invalidEventDuration](chhapticerror/code/invalideventduration.md)
  An event in the dictionary has an invalid duration.
- [CHHapticError.Code.invalidEventTime](chhapticerror/code/invalideventtime.md)
  The time of an event in the dictionary is invalid.
- [CHHapticError.Code.invalidEventType](chhapticerror/code/invalideventtype.md)
  The type of an event in the dictionary is invalid.
- [CHHapticError.Code.invalidParameterType](chhapticerror/code/invalidparametertype.md)
  A pattern dictionary or parameter array contains an unknown or invalid parameter type.
- [CHHapticError.Code.invalidPatternDictionary](chhapticerror/code/invalidpatterndictionary.md)
  A pattern in the dictionary is missing a required field.
- [CHHapticError.Code.invalidPatternPlayer](chhapticerror/code/invalidpatternplayer.md)
  The current pattern player is no longer valid due to a server error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticerror/code/invalidpatterndata)*