# endInterruption()

**Framework**: AVFAudio  
**Kind**: method

Called after your audio session interruption ends.

**Availability**:
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func endInterruption()
```

#### Discussion

The [`endInterruption(withFlags:)`](avaudiosessiondelegate/endinterruption(withflags:).md) method provides you with more information upon interruption end than this method does. Apple recommends that you use [`endInterruption(withFlags:)`](avaudiosessiondelegate/endinterruption(withflags:).md) instead of this method.

If you implement the [`endInterruption(withFlags:)`](avaudiosessiondelegate/endinterruption(withflags:).md) method, that method is called instead of this one when an interruption ends.

To resume using audio after an interruption ends, you must ensure that your audio session is active. [`AVAudioPlayer`](avaudioplayer.md) and [`AVAudioRecorder`](avaudiorecorder.md) instances reactivate your audio session automatically when an interruption ends. If you are using another audio technology, such as OpenAL, audio units, or audio queues, you must reactivate your audio session yourself before you can again use audio.

You can also use this method to update the user interface and application state, as necessary.

## See Also

- [func beginInterruption()](avaudiosessiondelegate/begininterruption.md)
  Called after your audio session is interrupted.
- [func endInterruption(withFlags: Int)](avaudiosessiondelegate/endinterruption(withflags:).md)
  Called after your audio session interruption ends, with flags indicating the state of the audio session.
- [func inputIsAvailableChanged(Bool)](avaudiosessiondelegate/inputisavailablechanged(_:).md)
  Called after the availability of audio input changes on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessiondelegate/endinterruption())*