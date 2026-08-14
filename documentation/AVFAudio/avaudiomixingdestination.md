# AVAudioMixingDestination

**Framework**: AVFAudio  
**Kind**: class

An object that represents a connection to a mixer node from a node that conforms to the audio mixing protocol.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class AVAudioMixingDestination
```

#### Overview

You can only use a destination instance when a source node provides it. You can’t use it as a standalone instance.

## Topics

### Getting Mixing Destination Properties
- [var connectionPoint: AVAudioConnectionPoint](avaudiomixingdestination/connectionpoint.md)
  The underlying mixer connection point.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [AVAudio3DMixing](avaudio3dmixing.md)
- [AVAudioMixing](avaudiomixing.md)
- [AVAudioStereoMixing](avaudiostereomixing.md)
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func destination(forMixer: AVAudioNode, bus: AVAudioNodeBus) -> AVAudioMixingDestination?](avaudiomixing/destination(formixer:bus:).md)
  Gets the audio mixing destination object that corresponds to the specified mixer node and input bus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiomixingdestination)*