# AudioComponentValidationResult

**Framework**: Audio Toolbox  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum AudioComponentValidationResult
```

```c
enum AudioComponentValidationResult : UInt32;
```

## Topics

### Constants
- [AudioComponentValidationResult.failed](./audiocomponentvalidationresult/failed.md)
- [AudioComponentValidationResult.passed](./audiocomponentvalidationresult/passed.md)
- [AudioComponentValidationResult.timedOut](./audiocomponentvalidationresult/timedout.md)
- [AudioComponentValidationResult.unauthorizedError_Init](./audiocomponentvalidationresult/unauthorizederror_init.md)
- [AudioComponentValidationResult.unauthorizedError_Open](./audiocomponentvalidationresult/unauthorizederror_open.md)
- [AudioComponentValidationResult.unknown](./audiocomponentvalidationresult/unknown.md)
### Initializers
- [init?(rawValue: UInt32)](./audiocomponentvalidationresult/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Validating an Audio Component
- [func AudioComponentValidate(AudioComponent, CFDictionary?, UnsafeMutablePointer<AudioComponentValidationResult>) -> OSStatus](./audiocomponentvalidate%28_,_,_%29.md)
- [var kAudioComponentValidationParameter_LoadOutOfProcess: String](./kaudiocomponentvalidationparameter_loadoutofprocess.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult)*