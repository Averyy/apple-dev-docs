# AVMIDIControlChangeEvent.MessageType

**Framework**: AVFAudio  
**Kind**: enum

Constants that represents control change event types.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum MessageType
```

## Topics

### Event Types
- [AVMIDIControlChangeEvent.MessageType.bankSelect](avmidicontrolchangeevent/messagetype-swift.enum/bankselect.md)
  An event type for switching bank selection.
- [AVMIDIControlChangeEvent.MessageType.modWheel](avmidicontrolchangeevent/messagetype-swift.enum/modwheel.md)
  An event type for modulating a vibrato effect.
- [AVMIDIControlChangeEvent.MessageType.breath](avmidicontrolchangeevent/messagetype-swift.enum/breath.md)
  An event type for a breath controller.
- [AVMIDIControlChangeEvent.MessageType.foot](avmidicontrolchangeevent/messagetype-swift.enum/foot.md)
  An event type for sending continuous stream of values when using a foot controller.
- [AVMIDIControlChangeEvent.MessageType.portamentoTime](avmidicontrolchangeevent/messagetype-swift.enum/portamentotime.md)
  An event type for controlling the portamento rate.
- [AVMIDIControlChangeEvent.MessageType.dataEntry](avmidicontrolchangeevent/messagetype-swift.enum/dataentry.md)
  An event type for controlling the data entry parameters.
- [AVMIDIControlChangeEvent.MessageType.volume](avmidicontrolchangeevent/messagetype-swift.enum/volume.md)
  An event type for controlling the channel volume.
- [AVMIDIControlChangeEvent.MessageType.balance](avmidicontrolchangeevent/messagetype-swift.enum/balance.md)
  An event type for controlling the left and right channel balance.
- [AVMIDIControlChangeEvent.MessageType.pan](avmidicontrolchangeevent/messagetype-swift.enum/pan.md)
  An event type for controlling the left and right channel pan.
- [AVMIDIControlChangeEvent.MessageType.expression](avmidicontrolchangeevent/messagetype-swift.enum/expression.md)
  An event type that represents an expression controller.
- [AVMIDIControlChangeEvent.MessageType.sustain](avmidicontrolchangeevent/messagetype-swift.enum/sustain.md)
  An event type for switching a damper pedal on or off.
- [AVMIDIControlChangeEvent.MessageType.portamento](avmidicontrolchangeevent/messagetype-swift.enum/portamento.md)
  An event type for switching portamento on or off.
- [AVMIDIControlChangeEvent.MessageType.sostenuto](avmidicontrolchangeevent/messagetype-swift.enum/sostenuto.md)
  An event type for switching sostenuto on or off.
- [AVMIDIControlChangeEvent.MessageType.soft](avmidicontrolchangeevent/messagetype-swift.enum/soft.md)
  An event type for lowering the volume of the notes.
- [AVMIDIControlChangeEvent.MessageType.legatoPedal](avmidicontrolchangeevent/messagetype-swift.enum/legatopedal.md)
  An event type for switching the legato pedal on or off.
- [AVMIDIControlChangeEvent.MessageType.hold2Pedal](avmidicontrolchangeevent/messagetype-swift.enum/hold2pedal.md)
  An event type for holding notes.
- [AVMIDIControlChangeEvent.MessageType.filterResonance](avmidicontrolchangeevent/messagetype-swift.enum/filterresonance.md)
  An event type for a filter resonance.
- [AVMIDIControlChangeEvent.MessageType.releaseTime](avmidicontrolchangeevent/messagetype-swift.enum/releasetime.md)
  An event type for controlling the release time.
- [AVMIDIControlChangeEvent.MessageType.attackTime](avmidicontrolchangeevent/messagetype-swift.enum/attacktime.md)
  An event type for controlling the attack time.
- [AVMIDIControlChangeEvent.MessageType.brightness](avmidicontrolchangeevent/messagetype-swift.enum/brightness.md)
  An event type for controlling the brightness.
- [AVMIDIControlChangeEvent.MessageType.decayTime](avmidicontrolchangeevent/messagetype-swift.enum/decaytime.md)
  An event type for controlling the decay time.
- [AVMIDIControlChangeEvent.MessageType.vibratoRate](avmidicontrolchangeevent/messagetype-swift.enum/vibratorate.md)
  An event type for controlling the vibrato rate.
- [AVMIDIControlChangeEvent.MessageType.vibratoDepth](avmidicontrolchangeevent/messagetype-swift.enum/vibratodepth.md)
  An event type for controlling the vibrato depth.
- [AVMIDIControlChangeEvent.MessageType.vibratoDelay](avmidicontrolchangeevent/messagetype-swift.enum/vibratodelay.md)
  An event type for controlling the vibrato delay.
- [AVMIDIControlChangeEvent.MessageType.reverbLevel](avmidicontrolchangeevent/messagetype-swift.enum/reverblevel.md)
  An event type for controlling the reverb level.
- [AVMIDIControlChangeEvent.MessageType.chorusLevel](avmidicontrolchangeevent/messagetype-swift.enum/choruslevel.md)
  An event type for controlling the chorus level.
- [AVMIDIControlChangeEvent.MessageType.RPN_LSB](avmidicontrolchangeevent/messagetype-swift.enum/rpn_lsb.md)
  An event type that represents the registered parameter number LSB.
- [AVMIDIControlChangeEvent.MessageType.RPN_MSB](avmidicontrolchangeevent/messagetype-swift.enum/rpn_msb.md)
  An event type that represents the registered parameter number MSB.
- [AVMIDIControlChangeEvent.MessageType.allSoundOff](avmidicontrolchangeevent/messagetype-swift.enum/allsoundoff.md)
  An event type for muting all sounding notes.
- [AVMIDIControlChangeEvent.MessageType.resetAllControllers](avmidicontrolchangeevent/messagetype-swift.enum/resetallcontrollers.md)
  An event type for resetting all controllers to their default state.
- [AVMIDIControlChangeEvent.MessageType.allNotesOff](avmidicontrolchangeevent/messagetype-swift.enum/allnotesoff.md)
  An event type for muting all sounding notes while maintaining the release time.
- [AVMIDIControlChangeEvent.MessageType.omniModeOff](avmidicontrolchangeevent/messagetype-swift.enum/omnimodeoff.md)
  An event type for setting omni off mode.
- [AVMIDIControlChangeEvent.MessageType.omniModeOn](avmidicontrolchangeevent/messagetype-swift.enum/omnimodeon.md)
  An event type for setting omni on mode.
- [AVMIDIControlChangeEvent.MessageType.monoModeOn](avmidicontrolchangeevent/messagetype-swift.enum/monomodeon.md)
  An event type for setting the device mode to monophonic.
- [AVMIDIControlChangeEvent.MessageType.monoModeOff](avmidicontrolchangeevent/messagetype-swift.enum/monomodeoff.md)
  An event type for setting the device mode to polyphonic.
### Initializers
- [init?(rawValue: Int)](avmidicontrolchangeevent/messagetype-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var value: UInt32](avmidicontrolchangeevent/value.md)
  The value of the control change event.
- [var messageType: AVMIDIControlChangeEvent.MessageType](avmidicontrolchangeevent/messagetype-swift.property.md)
  The type of control change message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidicontrolchangeevent/messagetype-swift.enum)*