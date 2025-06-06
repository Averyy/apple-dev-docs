# requestAccess(for:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Requests the user’s permission to allow the app to capture media of a particular type.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.14+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class func requestAccess(for mediaType: AVMediaType) async -> Bool
```

## Mentions

- [Requesting authorization to capture and save media](requesting-authorization-to-capture-and-save-media.md)

#### Discussion

Capturing media requires explicit permission from the user. An app’s default authorization status is [`AVAuthorizationStatus.notDetermined`](avauthorizationstatus/notdetermined.md), which means the user hasn’t yet granted it permission to capture media. The first time you create an [`AVCaptureDeviceInput`](avcapturedeviceinput.md) object for a media type that requires permission, the system automatically displays an alert to request recording permission. Alternatively, call this method to prompt the user at a time of your choosing. The system saves the user’s selection so that it doesn’t have to prompt the user again. A user can change their authorization status in the Settings app.

> ❗ **Important**:  Your app must provide an explanation for its use of capture devices using the [`NSCameraUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSCameraUsageDescription) and [`NSMicrophoneUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMicrophoneUsageDescription) Info.plist keys. The system presents the strings you set for these keys when prompting the user for permission, and thereafter in the Settings app. Calling this method or attempting to start a capture session without a usage description raises an exception.

 Your app must provide an explanation for its use of capture devices using the [`NSCameraUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSCameraUsageDescription) and [`NSMicrophoneUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMicrophoneUsageDescription) Info.plist keys. The system presents the strings you set for these keys when prompting the user for permission, and thereafter in the Settings app. Calling this method or attempting to start a capture session without a usage description raises an exception.

Calling this method doesn’t block the thread while the system is prompting the user for access. However, until the grants permission, the system only vends black video frames and silent audio samples.

> **Note**:  Calling this method with a media type of [`audio`](avmediatype/audio.md) is equivalent to calling the [`requestRecordPermission(_:)`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession/requestRecordPermission(_:)) method on [`AVAudioSession`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession).

 Calling this method with a media type of [`audio`](avmediatype/audio.md) is equivalent to calling the [`requestRecordPermission(_:)`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession/requestRecordPermission(_:)) method on [`AVAudioSession`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession).

## Parameters

- `mediaType`: A media type for which to check the authorization status. The supported media types are   and  .
- `handler`: Return control to the main queue or   before performing user interface updates.

## See Also

- [class func authorizationStatus(for: AVMediaType) -> AVAuthorizationStatus](avcapturedevice/authorizationstatus(for:).md)
  Returns an authorization status that indicates whether the user grants the app permission to capture media of a particular type.
- [enum AVAuthorizationStatus](avauthorizationstatus.md)
  Constants that indicate the status of an app’s authorization to capture media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/requestaccess(for:completionhandler:))*