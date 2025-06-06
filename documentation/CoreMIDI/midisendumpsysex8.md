# MIDISendUMPSysex8(_:)

**Framework**: Core MIDI  
**Kind**: func

Asynchronously sends a single universal MIDI packet (UMP) system-exclusive (SysEx) event with an 8-bit message.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func MIDISendUMPSysex8(_ umpRequest: UnsafeMutablePointer<MIDISysexSendRequestUMP>) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

#### Discussion

The request’s [`data`](midisysexsendrequest/data.md) needs to point to a single MIDI SysEx 8-bit message, or portion thereof.

## Parameters

- `umpRequest`: Contains the destination and a pointer to the MIDI data to send.

## See Also

- [func MIDISendUMPSysex(UnsafeMutablePointer<MIDISysexSendRequestUMP>) -> OSStatus](midisendumpsysex(_:).md)
  Asynchronously sends a single universal MIDI packet (UMP) system-exclusive (SysEx) event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midisendumpsysex8(_:))*