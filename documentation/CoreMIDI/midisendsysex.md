# MIDISendSysex(_:)

**Framework**: Core MIDI  
**Kind**: func

Asynchronously sends a single system-exclusive (SysEx) event.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func MIDISendSysex(_ request: UnsafeMutablePointer<MIDISysexSendRequest>) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

## Parameters

- `request`: Contains the destination and a pointer to the MIDI data to send.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midisendsysex(_:))*