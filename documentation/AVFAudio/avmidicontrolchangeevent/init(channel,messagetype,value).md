# init(channel:messageType:value:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithChannel:(UInt32) channel messageType:(AVMIDIControlChangeMessageType) messageType value:(UInt32) value;
```

## Parameters

- `channel`: The MIDI channel for the control change, between `0` and `15`.
- `messageType`: The type that indicates which MIDI control change message to send.
- `value`: The value for the control change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidicontrolchangeevent/init(channel:messagetype:value:))*