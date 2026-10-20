# beginInterruption()

**Framework**: AVFAudio  
**Kind**: method

Called after your audio session is interrupted.

**Availability**:
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func beginInterruption()
```

#### Discussion

By the time this interruption arrives, your audio has already stopped. Your application may be suspended or terminated following an interruption—for example, if a user chooses to take an incoming phone call. Use this method to adjust the user interface, and to save application state, as necessary.

## See Also

- [Audio Session Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Audio/Conceptual/AudioSessionProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007875)
- [func endInterruption()](avaudiosessiondelegate/endinterruption.md)
  Called after your audio session interruption ends.
- [func endInterruption(withFlags: Int)](avaudiosessiondelegate/endinterruption(withflags:).md)
  Called after your audio session interruption ends, with flags indicating the state of the audio session.
- [func inputIsAvailableChanged(Bool)](avaudiosessiondelegate/inputisavailablechanged(_:).md)
  Called after the availability of audio input changes on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessiondelegate/begininterruption())*