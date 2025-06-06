# init(channel:key:velocity:duration:)

**Framework**: AVFAudio  
**Kind**: init

Creates an event with a MIDI channel, key number, velocity, and duration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(channel: UInt32, key keyNum: UInt32, velocity: UInt32, duration: AVMusicTimeStamp)
```

## Parameters

- `channel`: The MIDI channel, between   and  .
- `keyNum`: The MIDI key number, between   and  .
- `velocity`: The MIDI velocity, between   and  .
- `duration`: The duration for this note, in beats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidinoteevent/init(channel:key:velocity:duration:))*