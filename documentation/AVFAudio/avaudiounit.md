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

### Accessing the underlying Audio Unit
- [func withAudioUnit<R, E>((borrowing AudioUnit) throws(E) -> R) throws(E) -> R](avaudiounit/withaudiounit(_:)-66uo7.md)
  Provides scoped access to the audio unit’s AudioUnit
- [func withAudioUnit<R, E>((borrowing AudioUnit) throws(E) -> R) throws(E) -> R](avaudiounit/withaudiounit(_:)-6c2ze.md)
  Provides scoped access to the audio unit’s AudioUnit
- [var audioUnit: AudioUnit](avaudiounit/audiounit-5vuo0.md)
- [var audioUnit: AudioUnit](avaudiounit/audiounit-7dsac.md)
### Loading an audio preset file
- [func loadPreset(at: URL) throws](avaudiounit/loadpreset(at:).md)
  Loads an audio unit using a specified preset.
### Creating an Audio Unit component
- [class func instantiate(with: AudioComponentDescription, options: AudioComponentInstantiationOptions, completionHandler: (AVAudioUnit?, (any Error)?) -> Void)](avaudiounit/instantiate(with:options:completionhandler:).md)
  Creates an instance of an audio unit component asynchronously and wraps it in an audio unit class.
### Getting Audio Unit values
- [var audioComponentDescription: AudioComponentDescription](avaudiounit/audiocomponentdescription.md)
  The audio component description that represents the underlying Core Audio audio unit.
- [var manufacturerName: String](avaudiounit/manufacturername.md)
  The name of the manufacturer of the audio unit.
- [var name: String](avaudiounit/name.md)
  The name of the audio unit.
- [var version: Int](avaudiounit/version.md)
  The version number of the audio unit.

## Relationships

### Inherits From
- [AVAudioNode](avaudionode.md)
### Inherited By
- [AVAudioUnitEffect](avaudiouniteffect.md)
- [AVAudioUnitGenerator](avaudiounitgenerator.md)
- [AVAudioUnitMIDIInstrument](avaudiounitmidiinstrument.md)
- [AVAudioUnitTimeEffect](avaudiounittimeeffect.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Creating an Audio Unit extension](creating-an-audio-unit-extension.md)
  Build an extension by using an Xcode template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounit)*