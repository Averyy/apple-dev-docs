# MIDINotifyBlock

**Framework**: Core MIDI  
**Kind**: typealias

A callback block for notifying clients of state changes.

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
typealias MIDINotifyBlock = (UnsafePointer<MIDINotification>) -> Void
```

#### Discussion

The system calls this block when some aspect of the current MIDI setup changes. The system calls it on an arbitrary thread chosen by the implementation; thread safety is the responsibility of the block.

## Parameters

- `message`: A structure that contains information about what changed.

## See Also

- [struct MIDINotification](midinotification.md)
  A message that describes a system state change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinotifyblock)*