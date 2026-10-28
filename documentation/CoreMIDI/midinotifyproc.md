# MIDINotifyProc

**Framework**: Core MIDI  
**Kind**: typealias  
**Role**: Type Alias

A callback function for notifying clients of state changes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias MIDINotifyProc = (UnsafePointer<MIDINotification>, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*)(const struct MIDINotification *, void *) MIDINotifyProc;
```

## Discussion

The system invokes this callback when some aspect of the current MIDI setup changes. The system calls it on the same thread that you called [`MIDIClientCreate(_:_:_:_:)`](./midiclientcreate%28_,_,_,_%29.md) on.

## Parameters

- `message`: A structure that contains information about what changed.
- `refCon`: The client’s `refCon`, passed to [`MIDIClientCreate(_:_:_:_:)`](./midiclientcreate%28_,_,_,_%29.md).

## See Also

### Callbacks
- [struct MIDINotification](./midinotification.md)
  A message that describes a system state change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinotifyproc)*