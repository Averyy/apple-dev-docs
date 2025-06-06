# MIDINotifyProc

**Framework**: Core MIDI  
**Kind**: typealias

A callback function for notifying clients of state changes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias MIDINotifyProc = (UnsafePointer<MIDINotification>, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

The system invokes this callback when some aspect of the current MIDI setup changes. The system calls it on the same thread that you called [`MIDIClientCreate(_:_:_:_:)`](midiclientcreate(_:_:_:_:).md) on.

## Parameters

- `message`: A structure that contains information about what changed.
- `refCon`: The client’s  , passed to  .

## See Also

- [struct MIDINotification](midinotification.md)
  A message that describes a system state change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinotifyproc)*