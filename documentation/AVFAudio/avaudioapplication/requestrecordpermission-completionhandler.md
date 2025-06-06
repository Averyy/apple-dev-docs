# requestRecordPermission(completionHandler:)

**Framework**: AVFAudio  
**Kind**: method

Determines whether the app has permission to record audio.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
class func requestRecordPermission() async -> Bool
```

#### Discussion

Recording audio requires explicit permission from the user. The first time your app attempts to record audio input, the system automatically prompts the user for permission. You can also explicitly ask for permission by calling this method. This method returns immediately, but the system waits for user input if the user hasn’t previously granted or denied recording permission.

```swift
// Request permission to record.
if await AVAudioApplication.requestRecordPermission() {
    // The user grants access. Present recording interface.
} else {
    // The user denies access. Present a message that indicates
    // that they can change their permission settings in the
    // Privacy & Security section of the Settings app.
}
```

Unless a user grants your app permission to record audio, it captures only silence (zeroed out audio samples).

After a user responds to a recording permission prompt from your app, the system remembers their choice and won’t prompt them again. If a user denies the app recording permission, they can grant it access in the Privacy & Security section of the Settings app.

> ❗ **Important**:  Apps that access any of the device’s microphones must declare their intent to do so. You do this by including the `NSMicrophoneUsageDescription` key and a corresponding purpose string in your app’s `Info.plist`. When the system prompts the user to allow access, it displays the purpose string as part of the alert. If an application attempts to access any of the device’s microphones without a corresponding purpose string, the app exits.

 Apps that access any of the device’s microphones must declare their intent to do so. You do this by including the `NSMicrophoneUsageDescription` key and a corresponding purpose string in your app’s `Info.plist`. When the system prompts the user to allow access, it displays the purpose string as part of the alert.

If an application attempts to access any of the device’s microphones without a corresponding purpose string, the app exits.

## Parameters

- `response`: A Boolean value that indicates whether the user grants the app permission to record audio.

## See Also

- [var recordPermission: AVAudioApplication.recordPermission](avaudioapplication/recordpermission-swift.property.md)
  The app’s permission to record audio.
- [AVAudioApplication.recordPermission](avaudioapplication/recordpermission-swift.enum.md)
  Constants that indicate the app’s permission to record audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioapplication/requestrecordpermission(completionhandler:))*