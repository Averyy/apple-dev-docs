# requestRecordPermission(_:)

**Framework**: AVFAudio  
**Kind**: method

Requests the user’s permission to record audio.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func requestRecordPermission(_ response: @escaping (Bool) -> Void)
```

#### Discussion

Recording audio requires explicit permission from the user. The first time your app’s audio session attempts to record from an audio input, the system automatically prompts the user for permission. You can explicitly ask earlier by calling this method. Until the user grants your app permission to record, your app records only silence. When a user responds to a recording permission prompt for your app, the system remembers the choice. If the user has denied recording permission, they can reenable it in Settings > Privacy > Microphone.

This method returns immediately, but the `response` block waits for user input if the user hasn’t previously granted or denied recording permission.

The framework may call the thread from a different thread context. Dispatch back to the main thread for any changes that update the user interface.

```swift
// Request permission to record.
AVAudioSession.sharedInstance().requestRecordPermission { granted in
    if granted {
        // The user granted access. Present recording interface.
    } else {
        // Present message to user indicating that recording
        // can't be performed until they change their preference
        // under Settings -> Privacy -> Microphone
    }
}
```

> ❗ **Important**:  Apps that access any of the device’s microphones must declare their intent to do so. You do this by including the `NSMicrophoneUsageDescription` key and a corresponding purpose string in your app’s `Info.plist`. When the system prompts the user to allow access, it displays the purpose string as part of the alert. If an application attempts to access any of the device’s microphones without a corresponding purpose string, the app exits.

## Parameters

- `response`: When you call this method, if the user previously granted or denied recording permission, the block executes immediately without displaying a recording permission alert. If the user hasn’t yet granted or denied permission when you call this method, the system displays a recording permission alert and executes the block after the user responds to it.

## See Also

- [var recordPermission: AVAudioSession.RecordPermission](avaudiosession/recordpermission-swift.property.md)
  The current recording permission status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/requestrecordpermission(_:))*