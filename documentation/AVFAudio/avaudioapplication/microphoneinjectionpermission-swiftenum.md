# AVAudioApplication.MicrophoneInjectionPermission

**Framework**: AVFAudio  
**Kind**: enum

Constants that indicate an app’s permission to add audio to calls.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum MicrophoneInjectionPermission
```

## Topics

### Permissions
- [AVAudioApplication.MicrophoneInjectionPermission.serviceDisabled](avaudioapplication/microphoneinjectionpermission-swift.enum/servicedisabled.md)
  A person disables this service for all apps.
- [AVAudioApplication.MicrophoneInjectionPermission.undetermined](avaudioapplication/microphoneinjectionpermission-swift.enum/undetermined.md)
  The app hasn’t requested a person’s permission to add audio to calls.
- [AVAudioApplication.MicrophoneInjectionPermission.granted](avaudioapplication/microphoneinjectionpermission-swift.enum/granted.md)
  A person grants the app permission to add audio to calls.
- [AVAudioApplication.MicrophoneInjectionPermission.denied](avaudioapplication/microphoneinjectionpermission-swift.enum/denied.md)
  A person denies the app permission to add audio to calls.
### Initializers
- [init?(rawValue: Int)](avaudioapplication/microphoneinjectionpermission-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class func requestMicrophoneInjectionPermission(completionHandler: (AVAudioApplication.MicrophoneInjectionPermission) -> Void)](avaudioapplication/requestmicrophoneinjectionpermission(completionhandler:).md)
  Requests the app’s permission to add audio to calls.
- [var microphoneInjectionPermission: AVAudioApplication.MicrophoneInjectionPermission](avaudioapplication/microphoneinjectionpermission-swift.property.md)
  A value that indicates an app’s permission to add audio to calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioapplication/microphoneinjectionpermission-swift.enum)*