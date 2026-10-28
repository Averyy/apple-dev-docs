# requestMicrophoneInjectionPermission(completionHandler:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Type Method

Requests the app’s permission to add audio to calls.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.2+

## Declaration

```swift
class func requestMicrophoneInjectionPermission(completionHandler response: @escaping @Sendable (AVAudioApplication.MicrophoneInjectionPermission) -> Void)
```

```swift
class func requestMicrophoneInjectionPermission() async -> AVAudioApplication.MicrophoneInjectionPermission
```

```objc
+ (void) requestMicrophoneInjectionPermissionWithCompletionHandler:(void (^)(AVAudioApplicationMicrophoneInjectionPermission permission)) response;
```

## Discussion

The system immediately returns a response if a person has already granted or denied the app permission, or if the service is in a disabled state.  Otherwise, it presents a dialog to request permission and returns a result when a person dismisses the UI.

## See Also

### Managing microphone injection permission
- [var microphoneInjectionPermission: AVAudioApplication.MicrophoneInjectionPermission](./microphoneinjectionpermission-swift.property.md)
  A value that indicates an app’s permission to add audio to calls.
- [AVAudioApplication.MicrophoneInjectionPermission](./microphoneinjectionpermission-swift.enum.md)
  Constants that indicate an app’s permission to add audio to calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioapplication/requestmicrophoneinjectionpermission(completionhandler:))*