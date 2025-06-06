# silenceSecondaryAudioHintNotification

**Framework**: AVFAudio  
**Kind**: property

A notification the system posts when the primary audio from other apps starts and stops.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class let silenceSecondaryAudioHintNotification: NSNotification.Name
```

#### Discussion

Subscribe to this notification to ensure that the system notifies your app when optional secondary audio muting should begin or end. The system sends this notification only to registered listeners who are currently in the foreground and have an active audio session.

This notification’s [`userInfo`](https://developer.apple.com/documentation/foundation/nsnotification/1409222-userinfo) dictionary contains a [`AVAudioSession.SilenceSecondaryAudioHintType`](avaudiosession/silencesecondaryaudiohinttype.md) value for the [`AVAudioSessionSilenceSecondaryAudioHintTypeKey`](avaudiosessionsilencesecondaryaudiohinttypekey.md). Use the audio hint type to determine if your secondary audio muting should begin or end.

```swift
func handleSecondaryAudio(notification: Notification) {
    // Determine hint type
    guard let userInfo = notification.userInfo,
        let typeValue = userInfo[AVAudioSessionSilenceSecondaryAudioHintTypeKey] as? UInt,
        let type = AVAudioSession.SilenceSecondaryAudioHintType(rawValue: typeValue) else {
            return
    }
    
    if type == .begin {
        // Other app audio started playing - mute secondary audio.
    } else {
        // Other app audio stopped playing - restart secondary audio.
    }
}
```

The system posts this notification on the main thread.

## Topics

### User Info Keys
- [let AVAudioSessionSilenceSecondaryAudioHintTypeKey: String](avaudiosessionsilencesecondaryaudiohinttypekey.md)
  A user info key that you use to retrieve the silence secondary audio hint type.
### User Info Values
- [AVAudioSession.SilenceSecondaryAudioHintType](avaudiosession/silencesecondaryaudiohinttype.md)
  Constants that indicate whether optional secondary audio muting should begin or end.

## See Also

- [var isOtherAudioPlaying: Bool](avaudiosession/isotheraudioplaying.md)
  A Boolean value that indicates whether another app is playing audio.
- [var secondaryAudioShouldBeSilencedHint: Bool](avaudiosession/secondaryaudioshouldbesilencedhint.md)
  A Boolean value that indicates whether another app, with a nonmixable audio session, is playing audio.
- [var allowHapticsAndSystemSoundsDuringRecording: Bool](avaudiosession/allowhapticsandsystemsoundsduringrecording.md)
  A Boolean value that indicates whether system sounds and haptics play while recording from audio input.
- [func setAllowHapticsAndSystemSoundsDuringRecording(Bool) throws](avaudiosession/setallowhapticsandsystemsoundsduringrecording(_:).md)
  Sets a Boolean value that indicates whether system sounds and haptics play while recording from audio input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/silencesecondaryaudiohintnotification)*