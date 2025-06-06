# AVAUPresetEvent

**Framework**: AVFAudio  
**Kind**: class

An object that represents a preset load and change on the music track’s destination audio unit.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class AVAUPresetEvent
```

## Topics

### Creating a Preset Event
- [init(scope: UInt32, element: UInt32, dictionary: [AnyHashable : Any])](avaupresetevent/init(scope:element:dictionary:).md)
  Creates an event with the scope, element, and dictionary for the preset.
### Configuring a Preset Event
- [var scope: UInt32](avaupresetevent/scope.md)
  The audio unit scope.
- [var element: UInt32](avaupresetevent/element.md)
  The element index in the scope.
- [var presetDictionary: [AnyHashable : Any]](avaupresetevent/presetdictionary.md)
  The dictionary that contains the preset.

## Relationships

### Inherits From
- [AVMusicEvent](avmusicevent.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVMusicEvent](avmusicevent.md)
  A base class for the events you associate with a music track.
- [class AVMusicUserEvent](avmusicuserevent.md)
  An object that represents a custom user message.
- [class AVParameterEvent](avparameterevent.md)
  An object that represents a parameter event on a music track’s destination.
- [class AVExtendedTempoEvent](avextendedtempoevent.md)
  An object that represents a tempo change to a specific beats-per-minute value.
- [class AVExtendedNoteOnEvent](avextendednoteonevent.md)
  An object that represents a custom extension of a MIDI note on event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaupresetevent)*