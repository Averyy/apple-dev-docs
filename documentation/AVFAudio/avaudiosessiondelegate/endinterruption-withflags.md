# endInterruption(withFlags:)

**Framework**: AVFAudio  
**Kind**: method

Called after your audio session interruption ends, with flags indicating the state of the audio session.

**Availability**:
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func endInterruption(withFlags flags: Int)
```

#### Discussion

To resume using audio after an interruption ends, you must ensure that your audio session is active. [`AVAudioPlayer`](avaudioplayer.md) and [`AVAudioRecorder`](avaudiorecorder.md) instances reactivate your audio session automatically when an interruption ends. If you are using another audio technology, such as OpenAL, audio units, or audio queues, you must reactivate your audio session yourself before you can again use audio.

You can also use this method to update the user interface and application state, as necessary.

If this delegate method receives the [`AVAudioSessionInterruptionFlags_ShouldResume`](avaudiosessioninterruptionflags_shouldresume.md) constant in its `flags` parameter, the audio session is immediately ready to be used.

If you implement this method, it is called instead of the [`endInterruption()`](avaudiosessiondelegate/endinterruption().md) method when an interruption ends.

## Parameters

- `flags`: Flags indicating the state of the audio session when this method is called. Flags are described in Interruption Flags.

## See Also

- [func beginInterruption()](avaudiosessiondelegate/begininterruption.md)
  Called after your audio session is interrupted.
- [func endInterruption()](avaudiosessiondelegate/endinterruption.md)
  Called after your audio session interruption ends.
- [func inputIsAvailableChanged(Bool)](avaudiosessiondelegate/inputisavailablechanged(_:).md)
  Called after the availability of audio input changes on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessiondelegate/endinterruption(withflags:))*