# init(channel:key:pressure:)

**Framework**: AVFAudio  
**Kind**: init

Creates an event with a channel, MIDI key number, and a key pressure value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(channel: UInt32, key: UInt32, pressure: UInt32)
```

## Parameters

- `channel`: The MIDI channel for the message, between   and  .
- `key`: The MIDI key number to apply the pressure to.
- `pressure`: The poly pressure value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidipolypressureevent/init(channel:key:pressure:))*