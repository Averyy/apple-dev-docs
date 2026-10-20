# AudioComponentValidate(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func AudioComponentValidate(_ inComponent: AudioComponent, _ inValidationParameters: CFDictionary?, _ outValidationResult: UnsafeMutablePointer<AudioComponentValidationResult>) -> OSStatus
```

```c
extern OSStatus AudioComponentValidate(AudioComponent inComponent, CFDictionaryRef inValidationParameters, AudioComponentValidationResult *outValidationResult);
```

## See Also

### Validating an Audio Component
- [var kAudioComponentValidationParameter_LoadOutOfProcess: String](./kaudiocomponentvalidationparameter_loadoutofprocess.md)
- [enum AudioComponentValidationResult](./audiocomponentvalidationresult.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidate(_:_:_:))*