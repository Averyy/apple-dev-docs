# AudioComponentValidationResult

**Framework**: Audio Toolbox  
**Kind**: enum

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum AudioComponentValidationResult
```

## Topics

### Constants
- [AudioComponentValidationResult.failed](audiocomponentvalidationresult/failed.md)
- [AudioComponentValidationResult.passed](audiocomponentvalidationresult/passed.md)
- [AudioComponentValidationResult.timedOut](audiocomponentvalidationresult/timedout.md)
- [AudioComponentValidationResult.unauthorizedError_Init](audiocomponentvalidationresult/unauthorizederror_init.md)
- [AudioComponentValidationResult.unauthorizedError_Open](audiocomponentvalidationresult/unauthorizederror_open.md)
- [AudioComponentValidationResult.unknown](audiocomponentvalidationresult/unknown.md)
### Initializers
- [init?(rawValue: UInt32)](audiocomponentvalidationresult/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func AudioComponentValidate(AudioComponent, CFDictionary?, UnsafeMutablePointer<AudioComponentValidationResult>) -> OSStatus](audiocomponentvalidate(_:_:_:).md)
- [var kAudioComponentValidationParameter_LoadOutOfProcess: String](kaudiocomponentvalidationparameter_loadoutofprocess.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidationresult)*