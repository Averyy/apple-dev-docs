# channel

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The MIDI channel.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var channel: UInt32 { get set }
```

```objc
@property (readwrite) UInt32 channel;
```

## See Also

### Configuring a MIDI note event
- [var key: UInt32](./key.md)
  The MIDI key number.
- [var velocity: UInt32](./velocity.md)
  The MIDI velocity.
- [var duration: AVMusicTimeStamp](./duration.md)
  The duration for the note, in beats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidinoteevent/channel)*