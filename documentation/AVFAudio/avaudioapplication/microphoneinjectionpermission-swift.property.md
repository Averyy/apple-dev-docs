# microphoneInjectionPermission

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A value that indicates an app’s permission to add audio to calls.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.2+

## Declaration

```swift
var microphoneInjectionPermission: AVAudioApplication.MicrophoneInjectionPermission { get }
```

```objc
@property (readonly) AVAudioApplicationMicrophoneInjectionPermission microphoneInjectionPermission;
```

## See Also

### Managing microphone injection permission
- [class func requestMicrophoneInjectionPermission(completionHandler: (AVAudioApplication.MicrophoneInjectionPermission) -> Void)](./requestmicrophoneinjectionpermission%28completionhandler%29.md)
  Requests the app’s permission to add audio to calls.
- [AVAudioApplication.MicrophoneInjectionPermission](./microphoneinjectionpermission-swift.enum.md)
  Constants that indicate an app’s permission to add audio to calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioapplication/microphoneinjectionpermission-swift.property)*