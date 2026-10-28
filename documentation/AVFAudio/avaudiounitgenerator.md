# AVAudioUnitGenerator

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVAudioUnitGenerator : AVAudioUnit
```

## Overview

A generator represents an [`AudioUnit`](../AudioToolbox/audiounit.md) of type `kAudioUnitType_Generator` or `kAudioUnitType_RemoteGenerator`. A generator has no audio input, but produces audio output. An example is a tone generator.

## Topics

### Creating an Audio Unit generator
- [init(audioComponentDescription: AudioComponentDescription)](./avaudiounitgenerator/init%28audiocomponentdescription%29.md)
  Creates a generator audio unit with the specified description.
### Bypassing the generator
- [var bypass: Bool](./avaudiounitgenerator/bypass.md)
  The bypass state of the audio unit.

## Relationships

### Inherits From
- [AVAudioUnit](./avaudiounit.md)
### Conforms To
- [AVAudio3DMixing](./avaudio3dmixing.md)
- [AVAudioMixing](./avaudiomixing.md)
- [AVAudioStereoMixing](./avaudiostereomixing.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitgenerator)*