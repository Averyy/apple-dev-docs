# beginInterruption()

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Called after your audio session is interrupted.

**Availability**:
- Mac Catalyst 14.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: No longer supported

## Declaration

```swift
optional func beginInterruption()
```

```objc
- (void) beginInterruption;
```

## Discussion

By the time this interruption arrives, your audio has already stopped. Your application may be suspended or terminated following an interruption—for example, if a user chooses to take an incoming phone call. Use this method to adjust the user interface, and to save application state, as necessary.

## See Also

### Related Documentation
- [Audio Session Programming Guide](https://developer.apple.com/library/archive/documentation/Audio/Conceptual/AudioSessionProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007875)
### Responding to session events
- [func endInterruption()](./endinterruption%28%29.md)
  Called after your audio session interruption ends.
- [func endInterruption(withFlags: Int)](./endinterruption%28withflags%29.md)
  Called after your audio session interruption ends, with flags indicating the state of the audio session.
- [func inputIsAvailableChanged(Bool)](./inputisavailablechanged%28_%29.md)
  Called after the availability of audio input changes on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessiondelegate/begininterruption())*