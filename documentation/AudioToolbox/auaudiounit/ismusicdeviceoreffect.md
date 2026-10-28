# isMusicDeviceOrEffect

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, readonly, getter=isMusicDeviceOrEffect) BOOL musicDeviceOrEffect;
```

*macOS*

```objc
@property (atomic, readonly, getter=isMusicDeviceOrEffect) BOOL musicDeviceOrEffect;
```

## Discussion

Returns [`true`](../../Swift/true.md) if the audio unit is a music device or effect.

## See Also

### Managing MIDI Events
- [var virtualMIDICableCount: Int](./virtualmidicablecount.md)
  The number of virtual MIDI cables implemented by a music device or effect.
- [var scheduleMIDIEventBlock: AUScheduleMIDIEventBlock?](./schedulemidieventblock.md)
  A block used to schedule MIDI events.
- [var midiOutputEventBlock: AUMIDIOutputEventBlock?](./midioutputeventblock.md)
- [var midiOutputNames: [String]](./midioutputnames.md)
  The names of the MIDI outputs.
- [typealias AUScheduleMIDIEventBlock](../auschedulemidieventblock.md)
  A block to schedule MIDI events.
- [typealias AUMIDIOutputEventBlock](../aumidioutputeventblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/ismusicdeviceoreffect)*