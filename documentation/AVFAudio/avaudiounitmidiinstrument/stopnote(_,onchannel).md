# stopNote(_:onChannel:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Sends a MIDI Note Off event to the instrument.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func stopNote(_ note: UInt8, onChannel channel: UInt8)
```

```objc
- (void) stopNote:(uint8_t) note onChannel:(uint8_t) channel;
```

## Parameters

- `note`: The note number (key) to stop. The valid range is `0` to `127`.
- `channel`: The channel number to send the event to. The valid range is `0` to `15`.

## See Also

### Starting and stopping play
- [func startNote(UInt8, withVelocity: UInt8, onChannel: UInt8)](./startnote%28_,withvelocity,onchannel%29.md)
  Sends a MIDI Note On event to the instrument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitmidiinstrument/stopnote(_:onchannel:))*