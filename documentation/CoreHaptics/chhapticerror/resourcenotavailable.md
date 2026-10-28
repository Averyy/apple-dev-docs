# resourceNotAvailable

**Framework**: Core Haptics  
**Kind**: property  
**Role**: Type Property

The framework didn’t locate a named resource.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static var resourceNotAvailable: CHHapticError.Code { get }
```

## Discussion

This error occurs when you specify an invalid audio file path.

## See Also

### Error Code Constants
- [static var badEventEntry: CHHapticError.Code](./badevententry.md)
  An event is missing a required field.
- [static var badParameterEntry: CHHapticError.Code](./badparameterentry.md)
  A parameter in an event is missing a required field.
- [static var engineNotRunning: CHHapticError.Code](./enginenotrunning.md)
  Your app requested haptic playback when the engine wasn’t running.
- [static var engineStartTimeout: CHHapticError.Code](./enginestarttimeout.md)
  The haptic engine timed out while starting.
- [static var fileNotFound: CHHapticError.Code](./filenotfound.md)
  The system couldn’t find an audio file or haptic asset.
- [static var insufficientPower: CHHapticError.Code](./insufficientpower.md)
  The operation failed due to power restrictions.
- [static var invalidAudioResource: CHHapticError.Code](./invalidaudioresource.md)
  A pattern dictionary or an event array contain a reference to an invalid audio resource.
- [static var invalidAudioSession: CHHapticError.Code](./invalidaudiosession.md)
  The system invalidated the audio session associated with the haptic engine.
- [static var invalidEngineParameter: CHHapticError.Code](./invalidengineparameter.md)
  Your app attempted to initialize the haptic engine with an invalid configuration parameter.
- [static var invalidEventDuration: CHHapticError.Code](./invalideventduration.md)
  An event in the dictionary has an invalid duration.
- [static var invalidEventTime: CHHapticError.Code](./invalideventtime.md)
  The time of an event in the dictionary is invalid.
- [static var invalidEventType: CHHapticError.Code](./invalideventtype.md)
  The type of an event in the dictionary is invalid.
- [static var invalidParameterType: CHHapticError.Code](./invalidparametertype.md)
  A pattern dictionary or parameter array contains an unknown or invalid parameter type.
- [static var invalidPatternData: CHHapticError.Code](./invalidpatterndata.md)
  Your app passed an invalid pattern to the haptic engine or player.
- [static var invalidPatternDictionary: CHHapticError.Code](./invalidpatterndictionary.md)
  A pattern in the dictionary is missing a required field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticerror/resourcenotavailable)*