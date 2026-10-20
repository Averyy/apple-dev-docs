# midiOutputNames

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, copy, readonly) NSArray<NSString *> * MIDIOutputNames;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSArray<NSString *> * MIDIOutputNames;
```

## See Also

### Managing MIDI Events
- [var isMusicDeviceOrEffect: Bool](./ismusicdeviceoreffect.md)
  Specifies whether an audio unit responds to MIDI events.
- [var virtualMIDICableCount: Int](./virtualmidicablecount.md)
  The number of virtual MIDI cables implemented by a music device or effect.
- [var scheduleMIDIEventBlock: AUScheduleMIDIEventBlock?](./schedulemidieventblock.md)
  A block used to schedule MIDI events.
- [var midiOutputEventBlock: AUMIDIOutputEventBlock?](./midioutputeventblock.md)
- [typealias AUScheduleMIDIEventBlock](../auschedulemidieventblock.md)
  A block to schedule MIDI events.
- [typealias AUMIDIOutputEventBlock](../aumidioutputeventblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/midioutputnames)*