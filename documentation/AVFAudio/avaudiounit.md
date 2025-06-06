# AVAudioUnit

**Framework**: AVFAudio  
**Kind**: class

A subclass of the audio node class that, processes audio either in real time or nonreal time, depending on the type of the audio unit.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAudioUnit
```

## Topics

### Getting the Core Audio audio unit
- [var audioUnit: AudioUnit](avaudiounit/audiounit.md)
  The underlying Core Audio audio unit.
### Loading an audio preset file
- [func loadPreset(at: URL) throws](avaudiounit/loadpreset(at:).md)
  Loads an audio unit using a specified preset.
### Creating an audio unit component
- [class func instantiate(with: AudioComponentDescription, options: AudioComponentInstantiationOptions, completionHandler: (AVAudioUnit?, (any Error)?) -> Void)](avaudiounit/instantiate(with:options:completionhandler:).md)
  Creates an instance of an audio unit component asynchronously and wraps it in an audio unit class.
### Getting audio unit values
- [var audioComponentDescription: AudioComponentDescription](avaudiounit/audiocomponentdescription.md)
  The audio component description that represents the underlying Core Audio audio unit.
- [var manufacturerName: String](avaudiounit/manufacturername.md)
  The name of the manufacturer of the audio unit.
- [var name: String](avaudiounit/name.md)
  The name of the audio unit.
- [var version: Int](avaudiounit/version.md)
  The version number of the audio unit.
- [var auAudioUnit: AUAudioUnit](avaudiounit/auaudiounit.md)
  The audio unit class wrapping or underlying the implementation’s audio unit.

## Relationships

### Inherits From
- [AVAudioNode](avaudionode.md)
### Inherited By
- [AVAudioUnitEffect](avaudiouniteffect.md)
- [AVAudioUnitGenerator](avaudiounitgenerator.md)
- [AVAudioUnitMIDIInstrument](avaudiounitmidiinstrument.md)
- [AVAudioUnitTimeEffect](avaudiounittimeeffect.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Creating an audio unit extension](creating-an-audio-unit-extension.md)
  Build an extension by using an Xcode template.
- [Using voice processing](using-voice-processing.md)
  Add voice-processing capabilities to your app by using audio engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounit)*