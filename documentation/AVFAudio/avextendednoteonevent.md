# AVExtendedNoteOnEvent

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

An object that represents a custom extension of a MIDI note on event.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class AVExtendedNoteOnEvent
```

```objc
@interface AVExtendedNoteOnEvent : AVMusicEvent
```

## Overview

Use this to allow an app to trigger a custom note on event on one of several Apple audio units that support it. The floating point note and velocity numbers allow for optional fractional control of the note’s runtime properties that the system modulates by those inputs. This event supports the possibility of an audio unit with more than the standard 16 MIDI channels.

## Topics

### Creating a note-on event
- [init(midiNote: Float, velocity: Float, groupID: UInt32, duration: AVMusicTimeStamp)](./avextendednoteonevent/init%28midinote,velocity,groupid,duration%29-60hve.md)
  Creates an event with a MIDI note, velocity, group identifier, and duration.
- [init(midiNote: Float, velocity: Float, instrumentID: UInt32, groupID: UInt32, duration: AVMusicTimeStamp)](./avextendednoteonevent/init%28midinote,velocity,instrumentid,groupid,duration%29-rqr5.md)
  Creates a note on event with the default instrument.
### Configuring a note-on event
- [var midiNote: Float](./avextendednoteonevent/midinote.md)
  The MIDI note number.
- [var velocity: Float](./avextendednoteonevent/velocity.md)
  The MDI velocity.
- [var instrumentID: UInt32](./avextendednoteonevent/instrumentid.md)
  The instrument identifier.
- [var groupID: UInt32](./avextendednoteonevent/groupid.md)
  The audio unit channel that handles the event.
- [var duration: AVMusicTimeStamp](./avextendednoteonevent/duration.md)
  The duration of the event, in beats.
### Getting the default instrument
- [class let defaultInstrument: UInt32](./avextendednoteonevent/defaultinstrument.md)
  A constant that represents the default instrument identifier.
### Initializers
- [init(MIDINote: Float, velocity: Float, groupID: UInt32, duration: AVMusicTimeStamp)](./avextendednoteonevent/init%28midinote,velocity,groupid,duration%29-985j8.md)
- [init(MIDINote: Float, velocity: Float, instrumentID: UInt32, groupID: UInt32, duration: AVMusicTimeStamp)](./avextendednoteonevent/init%28midinote,velocity,instrumentid,groupid,duration%29-3a40r.md)

## Relationships

### Inherits From
- [AVMusicEvent](./avmusicevent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Handling music events
- [class AVMusicEvent](./avmusicevent.md)
  A base class for the events you associate with a music track.
- [class AVMusicUserEvent](./avmusicuserevent.md)
  An object that represents a custom user message.
- [class AVParameterEvent](./avparameterevent.md)
  An object that represents a parameter event on a music track’s destination.
- [class AVAUPresetEvent](./avaupresetevent.md)
  An object that represents a preset load and change on the music track’s destination audio unit.
- [class AVExtendedTempoEvent](./avextendedtempoevent.md)
  An object that represents a tempo change to a specific beats-per-minute value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avextendednoteonevent)*