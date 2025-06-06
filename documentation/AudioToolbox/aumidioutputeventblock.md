# AUMIDIOutputEventBlock

**Framework**: Audio Toolbox  
**Kind**: typealias

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AUMIDIOutputEventBlock = (AUEventSampleTime, UInt8, Int, UnsafePointer<UInt8>) -> OSStatus
```

## See Also

- [var isMusicDeviceOrEffect: Bool](auaudiounit/ismusicdeviceoreffect.md)
  Specifies whether an audio unit responds to MIDI events.
- [var virtualMIDICableCount: Int](auaudiounit/virtualmidicablecount.md)
  The number of virtual MIDI cables implemented by a music device or effect.
- [var scheduleMIDIEventBlock: AUScheduleMIDIEventBlock?](auaudiounit/schedulemidieventblock.md)
  A block used to schedule MIDI events.
- [var midiOutputEventBlock: AUMIDIOutputEventBlock?](auaudiounit/midioutputeventblock.md)
- [var midiOutputNames: [String]](auaudiounit/midioutputnames.md)
  The names of the MIDI outputs.
- [typealias AUScheduleMIDIEventBlock](auschedulemidieventblock.md)
  A block to schedule MIDI events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/aumidioutputeventblock)*