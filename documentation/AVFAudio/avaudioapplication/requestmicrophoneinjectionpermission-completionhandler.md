# requestMicrophoneInjectionPermission(completionHandler:)

**Framework**: AVFAudio  
**Kind**: method

Requests the app’s permission to add audio to calls.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.2+

## Declaration

```swift
class func requestMicrophoneInjectionPermission() async -> AVAudioApplication.MicrophoneInjectionPermission
```

#### Discussion

The system immediately returns a response if a person has already granted or denied the app permission, or if the service is in a disabled state.  Otherwise, it presents a dialog to request permission and returns a result when a person dismisses the UI.

## See Also

- [var microphoneInjectionPermission: AVAudioApplication.MicrophoneInjectionPermission](avaudioapplication/microphoneinjectionpermission-swift.property.md)
  A value that indicates an app’s permission to add audio to calls.
- [AVAudioApplication.MicrophoneInjectionPermission](avaudioapplication/microphoneinjectionpermission-swift.enum.md)
  Constants that indicate an app’s permission to add audio to calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioapplication/requestmicrophoneinjectionpermission(completionhandler:))*