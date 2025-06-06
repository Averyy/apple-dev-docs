# AVAudioMixerNode

**Framework**: AVFAudio  
**Kind**: class

An object that takes any number of inputs and converts them into a single output.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class AVAudioMixerNode
```

#### Overview

The mixer accepts input at any sample rate and efficiently combines sample rate conversions. It also accepts any channel count and correctly upmixes or downmixes to the output channel count.

## Topics

### Creating a Mixer Node
- [init()](avaudiomixernode/init.md)
  Creates an audio mixer node.
### Getting and Setting the Mixer Volume
- [var outputVolume: Float](avaudiomixernode/outputvolume.md)
  The mixer’s output volume.
### Getting an Input Bus
- [var nextAvailableInputBus: AVAudioNodeBus](avaudiomixernode/nextavailableinputbus.md)
  An audio bus that isn’t in a connected state.

## Relationships

### Inherits From
- [AVAudioNode](avaudionode.md)
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

## See Also

- [protocol AVAudioMixing](avaudiomixing.md)
  A collection of properties that are applicable to the input bus of a mixer node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiomixernode)*