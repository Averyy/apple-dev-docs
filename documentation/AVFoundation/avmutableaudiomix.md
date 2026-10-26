# AVMutableAudioMix

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that manages the input parameters for mixing audio tracks.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class AVMutableAudioMix
```

```objc
@interface AVMutableAudioMix : AVAudioMix
```

## Topics

### Input parameters
- [var inputParameters: [AVAudioMixInputParameters]](./avmutableaudiomix/inputparameters.md)
  An array of input parameters for the mix.
### Creating a mix
- [+ audioMix](./avmutableaudiomix/audiomix.md)
  Returns a new mutable audio mix.

## Relationships

### Inherits From
- [AVAudioMix](./avaudiomix.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSMutableCopying](../Foundation/nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Mixing
- [class AVAudioMix](./avaudiomix.md)
  An object that manages the input parameters for mixing audio tracks.
- [class AVAudioMixInputParameters](./avaudiomixinputparameters.md)
  An object that represents the parameters that you apply when adding an audio track to a mix.
- [enum AVAudioMixInputParametersTrackID](./avaudiomixinputparameterstrackid.md)
  Special value for the trackID property of AVAudioMixInputParameters.
- [class AVMutableAudioMixInputParameters](./avmutableaudiomixinputparameters.md)
  The parameters you use when adding an audio track to a mix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutableaudiomix)*