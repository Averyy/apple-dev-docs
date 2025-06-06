# inputIsAvailableChanged(_:)

**Framework**: AVFAudio  
**Kind**: method

Called after the availability of audio input changes on a device.

**Availability**:
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func inputIsAvailableChanged(_ isInputAvailable: Bool)
```

## Parameters

- `isInputAvailable`:   if audio input is now available, or   if it is not.

## See Also

- [func beginInterruption()](avaudiosessiondelegate/begininterruption.md)
  Called after your audio session is interrupted.
- [func endInterruption()](avaudiosessiondelegate/endinterruption.md)
  Called after your audio session interruption ends.
- [func endInterruption(withFlags: Int)](avaudiosessiondelegate/endinterruption(withflags:).md)
  Called after your audio session interruption ends, with flags indicating the state of the audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessiondelegate/inputisavailablechanged(_:))*