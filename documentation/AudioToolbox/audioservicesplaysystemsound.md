# AudioServicesPlaySystemSound(_:)

**Framework**: Audio Toolbox  
**Kind**: func

Plays a system sound object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioServicesPlaySystemSound(_ inSystemSoundID: SystemSoundID)
```

#### Discussion

This function plays a short sound (30 seconds or less in duration). Because sound might play for several seconds, this function is executed asynchronously. To know when a sound has finished playing, call the [`AudioServicesAddSystemSoundCompletion(_:_:_:_:_:)`](audioservicesaddsystemsoundcompletion(_:_:_:_:_:).md) function to register a callback function.

On some iOS devices, you can pass the [`kSystemSoundID_Vibrate`](ksystemsoundid_vibrate.md) constant to invoke vibration. On other iOS devices, calling this function with that constant does nothing.

Sound files that you play using this function must be:

- No longer than 30 seconds in duration
- In linear PCM or IMA4 (IMA/ADPCM) format
- Packaged in a `.caf`, `.aif`, or `.wav` file

In addition, when you use the `AudioServicesPlaySystemSound` function:

- Sounds play at the current system audio volume, with no programmatic volume control available
- Sounds play immediately
- Looping and stereo positioning are unavailable
- Simultaneous playback is unavailable: You can play only one sound at a time
- The sound is played locally on the device speakers; it does not use audio routing.

## Parameters

- `inSystemSoundID`: The system sound to play. Before using this function, call the   function to obtain a system sound.

## See Also

- [func AudioServicesAddSystemSoundCompletion(SystemSoundID, CFRunLoop?, CFString?, AudioServicesSystemSoundCompletionProc, UnsafeMutableRawPointer?) -> OSStatus](audioservicesaddsystemsoundcompletion(_:_:_:_:_:).md)
  Registers a callback function that is invoked when a specified system sound finishes playing.
- [func AudioServicesCreateSystemSoundID(CFURL, UnsafeMutablePointer<SystemSoundID>) -> OSStatus](audioservicescreatesystemsoundid(_:_:).md)
  Creates a system sound object.
- [func AudioServicesPlayAlertSoundWithCompletion(SystemSoundID, (() -> Void)?)](audioservicesplayalertsoundwithcompletion(_:_:).md)
- [func AudioServicesPlaySystemSoundWithCompletion(SystemSoundID, (() -> Void)?)](audioservicesplaysystemsoundwithcompletion(_:_:).md)
- [func AudioServicesPlayAlertSound(SystemSoundID)](audioservicesplayalertsound(_:).md)
  Plays a system sound as an alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioservicesplaysystemsound(_:))*