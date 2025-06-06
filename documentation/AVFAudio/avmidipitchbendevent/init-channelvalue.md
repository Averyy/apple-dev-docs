# init(channel:value:)

**Framework**: AVFAudio  
**Kind**: init

Creates an event with a channel and pitch bend value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(channel: UInt32, value: UInt32)
```

## Parameters

- `channel`: The MIDI channel for the message, between   and  .
- `value`: The pitch bend value, between   and  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidipitchbendevent/init(channel:value:))*