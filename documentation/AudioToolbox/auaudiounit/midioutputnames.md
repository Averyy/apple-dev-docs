# midiOutputNames

**Framework**: Audio Toolbox  
**Kind**: property

The names of the MIDI outputs.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var midiOutputNames: [String] { get }
```

## See Also

- [var isMusicDeviceOrEffect: Bool](auaudiounit/ismusicdeviceoreffect.md)
  Specifies whether an audio unit responds to MIDI events.
- [var virtualMIDICableCount: Int](auaudiounit/virtualmidicablecount.md)
  The number of virtual MIDI cables implemented by a music device or effect.
- [var scheduleMIDIEventBlock: AUScheduleMIDIEventBlock?](auaudiounit/schedulemidieventblock.md)
  A block used to schedule MIDI events.
- [var midiOutputEventBlock: AUMIDIOutputEventBlock?](auaudiounit/midioutputeventblock.md)
- [typealias AUScheduleMIDIEventBlock](auschedulemidieventblock.md)
  A block to schedule MIDI events.
- [typealias AUMIDIOutputEventBlock](aumidioutputeventblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/midioutputnames)*