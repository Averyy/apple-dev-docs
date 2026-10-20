# inputIsAvailableChanged(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Called after the availability of audio input changes on a device.

**Availability**:
- Mac Catalyst 14.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: No longer supported

## Declaration

```swift
optional func inputIsAvailableChanged(_ isInputAvailable: Bool)
```

```objc
- (void) inputIsAvailableChanged:(BOOL) isInputAvailable;
```

## Parameters

- `isInputAvailable`: [`true`](../../Swift/true.md) if audio input is now available, or [`false`](../../Swift/false.md) if it is not.

## See Also

### Responding to session events
- [func beginInterruption()](./begininterruption%28%29.md)
  Called after your audio session is interrupted.
- [func endInterruption()](./endinterruption%28%29.md)
  Called after your audio session interruption ends.
- [func endInterruption(withFlags: Int)](./endinterruption%28withflags%29.md)
  Called after your audio session interruption ends, with flags indicating the state of the audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessiondelegate/inputisavailablechanged(_:))*