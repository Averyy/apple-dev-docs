# AVAudioApplication.MicrophoneInjectionPermission

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate an app’s permission to add audio to calls.

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
enum MicrophoneInjectionPermission
```

```c
enum AVAudioApplicationMicrophoneInjectionPermission : NSInteger;
```

## Topics

### Checking permission states
- [AVAudioApplication.MicrophoneInjectionPermission.serviceDisabled](./microphoneinjectionpermission-swift.enum/servicedisabled.md)
  A person disables this service for all apps.
- [AVAudioApplication.MicrophoneInjectionPermission.undetermined](./microphoneinjectionpermission-swift.enum/undetermined.md)
  The app hasn’t requested a person’s permission to add audio to calls.
- [AVAudioApplication.MicrophoneInjectionPermission.granted](./microphoneinjectionpermission-swift.enum/granted.md)
  A person grants the app permission to add audio to calls.
- [AVAudioApplication.MicrophoneInjectionPermission.denied](./microphoneinjectionpermission-swift.enum/denied.md)
  A person denies the app permission to add audio to calls.
### Creating a permission state
- [init?(rawValue: Int)](./microphoneinjectionpermission-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing microphone injection permission
- [class func requestMicrophoneInjectionPermission(completionHandler: (AVAudioApplication.MicrophoneInjectionPermission) -> Void)](./requestmicrophoneinjectionpermission%28completionhandler%29.md)
  Requests the app’s permission to add audio to calls.
- [var microphoneInjectionPermission: AVAudioApplication.MicrophoneInjectionPermission](./microphoneinjectionpermission-swift.property.md)
  A value that indicates an app’s permission to add audio to calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioapplication/microphoneinjectionpermission-swift.enum)*