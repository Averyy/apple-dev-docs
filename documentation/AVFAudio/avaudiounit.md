# AVAudioUnit

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVAudioUnit : AVAudioNode
```

## Topics

### Accessing the underlying Audio Unit
- [func withAudioUnit<R, E>((borrowing AudioUnit) throws(E) -> R) throws(E) -> R](./avaudiounit/withaudiounit%28_%29-66uo7.md)
  Provides scoped access to the audio unit’s AudioUnit
- [func withAudioUnit<R, E>((borrowing AudioUnit) throws(E) -> R) throws(E) -> R](./avaudiounit/withaudiounit%28_%29-6c2ze.md)
  Provides scoped access to the audio unit’s AudioUnit
- [var audioUnit: AudioUnit](./avaudiounit/audiounit-5vuo0.md)
- [var audioUnit: AudioUnit](./avaudiounit/audiounit-7dsac.md)
- [audioUnit](./avaudiounit/audiounit-4wpas.md)
  The underlying Core Audio audio unit.
### Loading an audio preset file
- [func loadPreset(at: URL) throws](./avaudiounit/loadpreset%28at%29.md)
  Loads an audio unit using a specified preset.
### Creating an Audio Unit component
- [class func instantiate(with: AudioComponentDescription, options: AudioComponentInstantiationOptions, completionHandler: (AVAudioUnit?, (any Error)?) -> Void)](./avaudiounit/instantiate%28with,options,completionhandler%29.md)
  Creates an instance of an audio unit component asynchronously and wraps it in an audio unit class.
### Getting Audio Unit values
- [var audioComponentDescription: AudioComponentDescription](./avaudiounit/audiocomponentdescription.md)
  The audio component description that represents the underlying Core Audio audio unit.
- [var manufacturerName: String](./avaudiounit/manufacturername.md)
  The name of the manufacturer of the audio unit.
- [var name: String](./avaudiounit/name.md)
  The name of the audio unit.
- [var version: Int](./avaudiounit/version.md)
  The version number of the audio unit.
- [AUAudioUnit](./avaudiounit/auaudiounit.md)
  The audio unit class wrapping or underlying the implementation’s audio unit.

## Relationships

### Inherits From
- [AVAudioNode](./avaudionode.md)
### Inherited By
- [AVAudioUnitEffect](./avaudiouniteffect.md)
- [AVAudioUnitGenerator](./avaudiounitgenerator.md)
- [AVAudioUnitMIDIInstrument](./avaudiounitmidiinstrument.md)
- [AVAudioUnitTimeEffect](./avaudiounittimeeffect.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Audio Unit setup
- [Creating an Audio Unit extension](./creating-an-audio-unit-extension.md)
  Build an extension by using an Xcode template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounit)*