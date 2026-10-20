# AVAudioMix

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
class AVAudioMix
```

```objc
@interface AVAudioMix : NSObject
```

## Topics

### Retrieving input parameters
- [var inputParameters: [AVAudioMixInputParameters]](./avaudiomix/inputparameters.md)
  An array of input parameters for the mix.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [AVMutableAudioMix](./avmutableaudiomix.md)
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
- [class AVAudioMixInputParameters](./avaudiomixinputparameters.md)
  An object that represents the parameters that you apply when adding an audio track to a mix.
- [enum AVAudioMixInputParametersTrackID](./avaudiomixinputparameterstrackid.md)
  Special value for the trackID property of AVAudioMixInputParameters.
- [class AVMutableAudioMix](./avmutableaudiomix.md)
  An object that manages the input parameters for mixing audio tracks.
- [class AVMutableAudioMixInputParameters](./avmutableaudiomixinputparameters.md)
  The parameters you use when adding an audio track to a mix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avaudiomix)*