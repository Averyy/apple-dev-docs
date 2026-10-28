# MIDISendUMPSysex(_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Asynchronously sends a single universal MIDI packet (UMP) system-exclusive (SysEx) event.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func MIDISendUMPSysex(_ umpRequest: UnsafeMutablePointer<MIDISysexSendRequestUMP>) -> OSStatus
```

```c
extern OSStatus MIDISendUMPSysex(MIDISysexSendRequestUMP *umpRequest);
```

## Return Value

An `OSStatus` result code.

## Discussion

The request’s [`words`](./midisysexsendrequestump/words.md) needs to point to a single MIDI SysEx message, or portion thereof.

## Parameters

- `umpRequest`: Contains the destination and a pointer to the MIDI data to send.

## See Also

### Sending a request
- [func MIDISendUMPSysex8(UnsafeMutablePointer<MIDISysexSendRequestUMP>) -> OSStatus](./midisendumpsysex8%28_%29.md)
  Asynchronously sends a single universal MIDI packet (UMP) system-exclusive (SysEx) event with an 8-bit message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midisendumpsysex(_:))*