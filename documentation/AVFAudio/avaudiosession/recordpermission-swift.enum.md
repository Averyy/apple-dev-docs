# AVAudioSession.RecordPermission

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

The values that define the current state of the record permission request.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum RecordPermission
```

```c
enum AVAudioSessionRecordPermission : NSUInteger;
```

#### Overview

The [`recordPermission`](./recordpermission-swift.property.md) property returns these values.

## Topics

### Creating a record permission
- [init?(rawValue: UInt)](./recordpermission-swift.enum/init%28rawvalue%29.md)
### Checking record permissions
- [AVAudioSession.RecordPermission.undetermined](./recordpermission-swift.enum/undetermined.md)
  A value that indicates that the user hasn’t granted or denied recording permission.
- [AVAudioSession.RecordPermission.denied](./recordpermission-swift.enum/denied.md)
  A value that indicates that the user has denied recording permission.
- [AVAudioSession.RecordPermission.granted](./recordpermission-swift.enum/granted.md)
  A value that indicates that the user has granted recording permission.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/recordpermission-swift.enum)*