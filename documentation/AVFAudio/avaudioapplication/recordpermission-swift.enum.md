# AVAudioApplication.recordPermission

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the app’s permission to record audio.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum recordPermission
```

```c
enum AVAudioApplicationRecordPermission : NSInteger;
```

## Topics

### Creating a permission state
- [init?(rawValue: Int)](./recordpermission-swift.enum/init%28rawvalue%29.md)
### Checking permission states
- [AVAudioApplication.recordPermission.undetermined](./recordpermission-swift.enum/undetermined.md)
  Indicates the app hasn’t requested recording permission.
- [AVAudioApplication.recordPermission.granted](./recordpermission-swift.enum/granted.md)
  Indicates the user grants the app permission to record audio.
- [AVAudioApplication.recordPermission.denied](./recordpermission-swift.enum/denied.md)
  Indicates the user denies the app permission to record audio.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Requesting audio recording permission
- [class func requestRecordPermission(completionHandler: (Bool) -> Void)](./requestrecordpermission%28completionhandler%29.md)
  Determines whether the app has permission to record audio.
- [var recordPermission: AVAudioApplication.recordPermission](./recordpermission-swift.property.md)
  The app’s permission to record audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioapplication/recordpermission-swift.enum)*