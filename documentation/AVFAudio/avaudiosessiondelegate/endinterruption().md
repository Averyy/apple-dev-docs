# endInterruption()

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Called after your audio session interruption ends.

**Availability**:
- Mac Catalyst 14.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: No longer supported

## Declaration

```swift
optional func endInterruption()
```

```objc
- (void) endInterruption;
```

## Discussion

The [`endInterruption(withFlags:)`](./endinterruption%28withflags%29.md) method provides you with more information upon interruption end than this method does. Apple recommends that you use [`endInterruption(withFlags:)`](./endinterruption%28withflags%29.md) instead of this method.

If you implement the [`endInterruption(withFlags:)`](./endinterruption%28withflags%29.md) method, that method is called instead of this one when an interruption ends.

To resume using audio after an interruption ends, you must ensure that your audio session is active. [`AVAudioPlayer`](../avaudioplayer.md) and [`AVAudioRecorder`](../avaudiorecorder.md) instances reactivate your audio session automatically when an interruption ends. If you are using another audio technology, such as OpenAL, audio units, or audio queues, you must reactivate your audio session yourself before you can again use audio.

You can also use this method to update the user interface and application state, as necessary.

## See Also

### Responding to session events
- [func beginInterruption()](./begininterruption%28%29.md)
  Called after your audio session is interrupted.
- [func endInterruption(withFlags: Int)](./endinterruption%28withflags%29.md)
  Called after your audio session interruption ends, with flags indicating the state of the audio session.
- [func inputIsAvailableChanged(Bool)](./inputisavailablechanged%28_%29.md)
  Called after the availability of audio input changes on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessiondelegate/endinterruption())*