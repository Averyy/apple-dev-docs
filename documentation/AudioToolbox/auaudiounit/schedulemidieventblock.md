# scheduleMIDIEventBlock

**Framework**: Audio Toolbox  
**Kind**: property

A block used to schedule MIDI events.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var scheduleMIDIEventBlock: AUScheduleMIDIEventBlock? { get }
```

#### Discussion

As with the render block, a host should fetch this block before beginning to render, if it intends to schedule MIDI events.

This property is implemented in the [`AUAudioUnit`](auaudiounit.md) base class. If the audio unit is not a music device or effect, this property is `nil`.

Subclasses should not override this property. When hosts schedule events via this block, they are delivered to the audio unit via the list of render events delivered to the [`internalRenderBlock`](auaudiounit/internalrenderblock.md) implementation.

## See Also

- [var isMusicDeviceOrEffect: Bool](auaudiounit/ismusicdeviceoreffect.md)
  Specifies whether an audio unit responds to MIDI events.
- [var virtualMIDICableCount: Int](auaudiounit/virtualmidicablecount.md)
  The number of virtual MIDI cables implemented by a music device or effect.
- [var midiOutputEventBlock: AUMIDIOutputEventBlock?](auaudiounit/midioutputeventblock.md)
- [var midiOutputNames: [String]](auaudiounit/midioutputnames.md)
  The names of the MIDI outputs.
- [typealias AUScheduleMIDIEventBlock](auschedulemidieventblock.md)
  A block to schedule MIDI events.
- [typealias AUMIDIOutputEventBlock](aumidioutputeventblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/schedulemidieventblock)*