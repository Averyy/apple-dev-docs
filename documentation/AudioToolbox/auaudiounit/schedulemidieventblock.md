# scheduleMIDIEventBlock

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, readonly, nullable) AUScheduleMIDIEventBlock scheduleMIDIEventBlock;
```

*macOS*

```objc
@property (atomic, readonly, nullable) AUScheduleMIDIEventBlock scheduleMIDIEventBlock;
```

## Discussion

As with the render block, a host should fetch this block before beginning to render, if it intends to schedule MIDI events.

This property is implemented in the [`AUAudioUnit`](../auaudiounit.md) base class. If the audio unit is not a music device or effect, this property is `nil`.

Subclasses should not override this property. When hosts schedule events via this block, they are delivered to the audio unit via the list of render events delivered to the [`internalRenderBlock`](./internalrenderblock.md) implementation.

## See Also

### Managing MIDI Events
- [var isMusicDeviceOrEffect: Bool](./ismusicdeviceoreffect.md)
  Specifies whether an audio unit responds to MIDI events.
- [var virtualMIDICableCount: Int](./virtualmidicablecount.md)
  The number of virtual MIDI cables implemented by a music device or effect.
- [var midiOutputEventBlock: AUMIDIOutputEventBlock?](./midioutputeventblock.md)
- [var midiOutputNames: [String]](./midioutputnames.md)
  The names of the MIDI outputs.
- [typealias AUScheduleMIDIEventBlock](../auschedulemidieventblock.md)
  A block to schedule MIDI events.
- [typealias AUMIDIOutputEventBlock](../aumidioutputeventblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/schedulemidieventblock)*