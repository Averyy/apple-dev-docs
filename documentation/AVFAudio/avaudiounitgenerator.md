# AVAudioUnitGenerator

**Framework**: AVFAudio  
**Kind**: class

An object that generates audio output.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAudioUnitGenerator
```

#### Overview

A generator represents an [`AudioUnit`](https://developer.apple.com/documentation/AudioToolbox/AudioUnit) of type `kAudioUnitType_Generator` or `kAudioUnitType_RemoteGenerator`. A generator has no audio input, but produces audio output. An example is a tone generator.

## Topics

### Creating an audio unit generator
- [init(audioComponentDescription: AudioComponentDescription)](avaudiounitgenerator/init(audiocomponentdescription:).md)
  Creates a generator audio unit with the specified description.
### Getting and setting the bypass status
- [var bypass: Bool](avaudiounitgenerator/bypass.md)
  The bypass state of the audio unit.

## Relationships

### Inherits From
- [AVAudioUnit](avaudiounit.md)
### Conforms To
- [AVAudio3DMixing](avaudio3dmixing.md)
- [AVAudioMixing](avaudiomixing.md)
- [AVAudioStereoMixing](avaudiostereomixing.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitgenerator)*