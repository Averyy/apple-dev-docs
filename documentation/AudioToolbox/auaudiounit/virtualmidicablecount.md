# virtualMIDICableCount

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

The number of virtual MIDI cables implemented by a music device or effect.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var virtualMIDICableCount: Int { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, readonly) NSInteger virtualMIDICableCount;
```

*macOS*

```objc
@property (atomic, readonly) NSInteger virtualMIDICableCount;
```

## Discussion

A music device or effect can support up to 256 virtual MIDI cables of input.

## See Also

### Managing MIDI Events
- [var isMusicDeviceOrEffect: Bool](./ismusicdeviceoreffect.md)
  Specifies whether an audio unit responds to MIDI events.
- [var scheduleMIDIEventBlock: AUScheduleMIDIEventBlock?](./schedulemidieventblock.md)
  A block used to schedule MIDI events.
- [var midiOutputEventBlock: AUMIDIOutputEventBlock?](./midioutputeventblock.md)
- [var midiOutputNames: [String]](./midioutputnames.md)
  The names of the MIDI outputs.
- [typealias AUScheduleMIDIEventBlock](../auschedulemidieventblock.md)
  A block to schedule MIDI events.
- [typealias AUMIDIOutputEventBlock](../aumidioutputeventblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/virtualmidicablecount)*