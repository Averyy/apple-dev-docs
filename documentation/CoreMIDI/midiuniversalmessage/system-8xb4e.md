# system

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

active when type is kMIDIMessageTypeSystem

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
struct { ... } system;
```

## Topics

### Instance Properties
- [songPositionPointer](./system-8xb4e/songpositionpointer.md)
  active when status is kMIDIStatusSongPosPointer
- [songSelect](./system-8xb4e/songselect.md)
  active when status is kMIDIStatusSongSelect
- [status](./system-8xb4e/status.md)
  determines which variant is active
- [timeCode](./system-8xb4e/timecode.md)
  active when status is kMIDIStatusMTC


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiuniversalmessage/system-8xb4e)*