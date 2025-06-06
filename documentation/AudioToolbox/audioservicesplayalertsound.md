# AudioServicesPlayAlertSound(_:)

**Framework**: Audiotoolbox  
**Kind**: func

Plays a system sound as an alert.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioServicesPlayAlertSound(_ inSystemSoundID: SystemSoundID)
```

#### Discussion

Depending on the particular iOS device, this function plays a short sound and may invoke vibration. Calling this function does the following on various iOS devices:

- —plays the specified sound. If the user has configured the Settings application for vibration on ring, also invokes vibration. However, the device does  vibrate if your app’s audio session is configured with the  [`playAndRecord`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession/Category-swift.struct/playAndRecord) or [`record`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession/Category-swift.struct/record) audio session category. This ensures that vibration doesn’t interfere with audio recording. For an explanation of audio session categories, see [`Categories Express Audio Roles`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Audio/Conceptual/AudioSessionProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007875-CH1-SW4).
- —plays a short alert melody.
- —plays the specified sound.

In iOS, the duration of the sound to be played must not be more than 30 seconds.

> **Note**:  System-supplied alert sounds and system-supplied user-interface sound effects are not available to your iOS application. For example, using the `kSystemSoundID_UserPreferredAlert` constant as a parameter to the `AudioServicesPlayAlertSound` function will not play anything.

In macOS, when a user has configured System Preferences to flash the screen for alerts, or if sound cannot be rendered, calling this function will result in the screen flashing. In macOS, pass the constant `kSystemSoundID_UserPreferredAlert` to play the alert sound selected by the user in System Preferences. In iOS there is no preferred user alert sound.

To play a short sound not used as an alert, use [`AudioServicesPlaySystemSound(_:)`](audioservicesplaysystemsound(_:).md).

## Parameters

- `inSystemSoundID`: Before using this function, call the   function to obtain a system sound.

## See Also

- [func AudioServicesCreateSystemSoundID(CFURL, UnsafeMutablePointer<SystemSoundID>) -> OSStatus](audioservicescreatesystemsoundid(_:_:).md)
  Creates a system sound object.
- [func AudioServicesPlayAlertSoundWithCompletion(SystemSoundID, (() -> Void)?)](audioservicesplayalertsoundwithcompletion(_:_:).md)
- [func AudioServicesPlaySystemSoundWithCompletion(SystemSoundID, (() -> Void)?)](audioservicesplaysystemsoundwithcompletion(_:_:).md)
- [func AudioServicesPlaySystemSound(SystemSoundID)](audioservicesplaysystemsound(_:).md)
  Plays a system sound object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioservicesplayalertsound(_:))*