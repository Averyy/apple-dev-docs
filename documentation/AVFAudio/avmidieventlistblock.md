# AVMIDIEventListBlock

**Framework**: AVFAudio  
**Kind**: typealias

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
typealias AVMIDIEventListBlock = (Int64, UInt8, UnsafePointer<MIDIEventList>) -> OSStatus
```

#### Discussion

A block used by an audio unit to send or receive MIDIEventList data.

## Parameters

- `eventSampleTime`: The time in samples at which the MIDI events are to occur.
- `cable`: The virtual cable number associated with this MIDI data.
- `eventList`: One full MIDI, partial MIDI SysEx, or a full SysEx UMP message.

## See Also

- [class AVAudioSequencer](avaudiosequencer.md)
  An object that plays audio from a collection of MIDI events the system organizes into music tracks.
- [class AVAudioUnitSampler](avaudiounitsampler.md)
  An object that you configure with one or more instrument samples, based on Apple’s Sampler audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidieventlistblock)*