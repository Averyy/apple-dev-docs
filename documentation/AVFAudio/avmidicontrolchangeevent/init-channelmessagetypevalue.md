# init(channel:messageType:value:)

**Framework**: AVFAudio  
**Kind**: init

Creates an event with a channel, control change type, and a value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(channel: UInt32, messageType: AVMIDIControlChangeEvent.MessageType, value: UInt32)
```

## Parameters

- `channel`: The MIDI channel for the control change, between   and  .
- `messageType`: The type that indicates which MIDI control change message to send.
- `value`: The value for the control change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidicontrolchangeevent/init(channel:messagetype:value:))*