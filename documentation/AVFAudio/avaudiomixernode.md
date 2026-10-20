# AVAudioMixerNode

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVAudioMixerNode : AVAudioNode
```

#### Overview

The mixer accepts input at any sample rate and efficiently combines sample rate conversions. It also accepts any channel count and correctly upmixes or downmixes to the output channel count.

## Topics

### Creating a mixer node
- [init()](./avaudiomixernode/init%28%29.md)
  Creates an audio mixer node.
### Adjusting the output volume
- [var outputVolume: Float](./avaudiomixernode/outputvolume.md)
  The mixer’s output volume.
### Getting an input bus
- [var nextAvailableInputBus: AVAudioNodeBus](./avaudiomixernode/nextavailableinputbus.md)
  An audio bus that isn’t in a connected state.

## Relationships

### Inherits From
- [AVAudioNode](./avaudionode.md)
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

## See Also

### Audio mixing
- [protocol AVAudioMixing](./avaudiomixing.md)
  A collection of properties that are applicable to the input bus of a mixer node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiomixernode)*