# isMusicDeviceOrEffect

**Framework**: Audio Toolbox  
**Kind**: property

Specifies whether an audio unit responds to MIDI events.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isMusicDeviceOrEffect: Bool { get }
```

#### Discussion

Returns [`true`](https://developer.apple.com/documentation/swift/true) if the audio unit is a music device or effect.

## See Also

- [var virtualMIDICableCount: Int](auaudiounit/virtualmidicablecount.md)
  The number of virtual MIDI cables implemented by a music device or effect.
- [var scheduleMIDIEventBlock: AUScheduleMIDIEventBlock?](auaudiounit/schedulemidieventblock.md)
  A block used to schedule MIDI events.
- [var midiOutputEventBlock: AUMIDIOutputEventBlock?](auaudiounit/midioutputeventblock.md)
- [var midiOutputNames: [String]](auaudiounit/midioutputnames.md)
  The names of the MIDI outputs.
- [typealias AUScheduleMIDIEventBlock](auschedulemidieventblock.md)
  A block to schedule MIDI events.
- [typealias AUMIDIOutputEventBlock](aumidioutputeventblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/ismusicdeviceoreffect)*