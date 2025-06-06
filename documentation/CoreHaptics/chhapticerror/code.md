# CHHapticError.Code

**Framework**: Core Haptics  
**Kind**: enum

Error codes for framework operations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

## Topics

### Error Codes
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
- [CHHapticError.Code.invalidPatternData](chhapticerror/code/invalidpatterndata.md)
  Your app passed an invalid pattern to the haptic engine or player.
- [CHHapticError.Code.invalidPatternDictionary](chhapticerror/code/invalidpatterndictionary.md)
  A pattern in the dictionary is missing a required field.
- [CHHapticError.Code.invalidPatternPlayer](chhapticerror/code/invalidpatternplayer.md)
  The current pattern player is no longer valid due to a server error.
- [CHHapticError.Code.invalidTime](chhapticerror/code/invalidtime.md)
  The time offset passed to the haptic engine is invalid.
- [CHHapticError.Code.memoryError](chhapticerror/code/memoryerror.md)
  The operation failed due to a lack of memory.
- [CHHapticError.Code.notSupported](chhapticerror/code/notsupported.md)
  The current device doesn’t support the haptic engine.
- [CHHapticError.Code.operationNotPermitted](chhapticerror/code/operationnotpermitted.md)
  Your app requested an operation that the haptic engine disallows.
- [CHHapticError.Code.resourceNotAvailable](chhapticerror/code/resourcenotavailable.md)
  The requested operation couldn’t finish due to a limit on available resources.
- [CHHapticError.Code.serverInterrupted](chhapticerror/code/serverinterrupted.md)
  Your app lost its connection to the haptic server.
- [CHHapticError.Code.serverInitFailed](chhapticerror/code/serverinitfailed.md)
  The haptic server failed to initialize.
- [CHHapticError.Code.unknownError](chhapticerror/code/unknownerror.md)
  An operation failed due to an unknown error.
### Initializers
- [init?(rawValue: Int)](chhapticerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let CoreHapticsErrorDomain: String](corehapticserrordomain.md)
  A string representation of the haptic error domain.
- [struct CHHapticError](chhapticerror.md)
  A structure that represents a framework error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticerror/code)*