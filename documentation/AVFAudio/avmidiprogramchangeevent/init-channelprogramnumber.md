# init(channel:programNumber:)

**Framework**: AVFAudio  
**Kind**: init

Creates a program change event with a channel and program number.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(channel: UInt32, programNumber: UInt32)
```

#### Discussion

The instrument this chooses depends on [`AVMIDIControlChangeEvent.MessageType.bankSelect`](avmidicontrolchangeevent/messagetype-swift.enum/bankselect.md) events sent prior to this event.

## Parameters

- `channel`: The MIDI channel for the message, between   and  .
- `programNumber`: The program number to send, between   and  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidiprogramchangeevent/init(channel:programnumber:))*