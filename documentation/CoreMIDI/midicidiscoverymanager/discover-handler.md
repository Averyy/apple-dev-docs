# discover(handler:)

**Framework**: Core MIDI  
**Kind**: method

Discovers the available MIDI-CI nodes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func discover(handler completedHandler: @escaping MIDICIDiscoveryResponseBlock)
```

## Parameters

- `completedHandler`: A closure the system calls when a MIDI-CI node discovery request is complete.

## Topics

### Handling Callbacks
- [typealias MIDICIDiscoveryResponseBlock](midicidiscoveryresponseblock.md)
  A block the system calls when a MIDI-CI node discovery request completes.
- [class MIDICIDiscoveredNode](midicidiscoverednode.md)
  A discovered MIDI-CI node that represents a MIDI source and destination that respond to capability inquiries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicidiscoverymanager/discover(handler:))*