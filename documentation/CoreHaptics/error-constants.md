# Error Constants

**Framework**: Core Haptics

Error code constants for framework operations.

## Topics

### Error Code Constants
- [static var badEventEntry: CHHapticError.Code](chhapticerror/badevententry.md)
  An event is missing a required field.
- [static var badParameterEntry: CHHapticError.Code](chhapticerror/badparameterentry.md)
  A parameter in an event is missing a required field.
- [static var engineNotRunning: CHHapticError.Code](chhapticerror/enginenotrunning.md)
  Your app requested haptic playback when the engine wasn’t running.
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
- [static var invalidTime: CHHapticError.Code](chhapticerror/invalidtime.md)
  The time offset passed to the haptic engine is invalid.
- [static var memoryError: CHHapticError.Code](chhapticerror/memoryerror.md)
  The operation failed due to a lack of memory.
- [static var notSupported: CHHapticError.Code](chhapticerror/notsupported.md)
  The current device doesn’t support the haptic engine.
- [static var operationNotPermitted: CHHapticError.Code](chhapticerror/operationnotpermitted.md)
  Your app requested an operation that the haptic engine disallows.
- [static var resourceNotAvailable: CHHapticError.Code](chhapticerror/resourcenotavailable.md)
  The framework didn’t locate a named resource.
- [static var serverInterrupted: CHHapticError.Code](chhapticerror/serverinterrupted.md)
  Your app lost its connection to the haptic server.
- [static var serverInitFailed: CHHapticError.Code](chhapticerror/serverinitfailed.md)
  The haptic server failed to initialize.
- [static var unknownError: CHHapticError.Code](chhapticerror/unknownerror.md)
  An operation failed due to an unknown error.

## See Also

- [CHHapticError.Code](chhapticerror/code.md)
  Error codes for framework operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/error-constants)*