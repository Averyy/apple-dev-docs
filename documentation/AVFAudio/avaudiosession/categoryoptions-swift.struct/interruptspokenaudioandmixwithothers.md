# interruptSpokenAudioAndMixWithOthers

**Framework**: AVFAudio  
**Kind**: property

An option that determines whether to pause spoken audio content from other sessions when your app plays its audio.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var interruptSpokenAudioAndMixWithOthers: AVAudioSession.CategoryOptions { get }
```

#### Discussion

You can set this option only if the audio session category is [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md), [`playback`](avaudiosession/category-swift.struct/playback.md), or [`multiRoute`](avaudiosession/category-swift.struct/multiroute.md). Setting this option also sets [`mixWithOthers`](avaudiosession/categoryoptions-swift.struct/mixwithothers.md).

If you clear this option, audio from your audio session interrupts other sessions. If you set this option, the system mixes your audio with other audio sessions, but interrupts (and stops) audio sessions that use the [`spokenAudio`](avaudiosession/mode-swift.struct/spokenaudio.md) audio session mode. It pauses the audio from other apps as long as your session is active. After your audio session deactivates, the system resumes the interrupted app’s audio.

Set this option if your app’s audio is occasional and spoken, such as in a turn-by-turn navigation app or an exercise app. This avoids intelligibility problems when two spoken audio apps mix. If you set this option, also set the [`duckOthers`](avaudiosession/categoryoptions-swift.struct/duckothers.md) option unless you have a specific reason not to. Ducking other audio, rather than interrupting it, is appropriate when the other audio isn’t spoken audio.

When you configure your audio session category using this option, notify other apps on the system when you deactivate your session so that they can resume audio playback. To do so, deactivate your session using the [`notifyOthersOnDeactivation`](avaudiosession/setactiveoptions/notifyothersondeactivation.md) option.

```swift
do {
    try session.setActive(false, options: .notifyOthersOnDeactivation)
} catch let error as NSError {
    print("Failed to deactivate audio session: \(error.localizedDescription)")
}
```

## See Also

- [static var mixWithOthers: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/mixwithothers.md)
  An option that indicates whether audio from this session mixes with audio from active sessions in other audio apps.
- [static var duckOthers: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/duckothers.md)
  An option that reduces the volume of other audio sessions while audio from this session plays.
- [static var allowBluetooth: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/allowbluetooth.md)
  An option that determines whether Bluetooth hands-free devices appear as available input routes.
- [static var allowBluetoothA2DP: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/allowbluetootha2dp.md)
  An option that determines whether you can stream audio from this session to Bluetooth devices that support the Advanced Audio Distribution Profile (A2DP).
- [static var allowAirPlay: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/allowairplay.md)
  An option that determines whether you can stream audio from this session to AirPlay devices.
- [static var defaultToSpeaker: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/defaulttospeaker.md)
  An option that determines whether audio from the session defaults to the built-in speaker instead of the receiver.
- [static var overrideMutedMicrophoneInterruption: AVAudioSession.CategoryOptions](avaudiosession/categoryoptions-swift.struct/overridemutedmicrophoneinterruption.md)
  An option that indicates whether the system interrupts the audio session when it mutes the built-in microphone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/categoryoptions-swift.struct/interruptspokenaudioandmixwithothers)*