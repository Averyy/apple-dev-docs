# MIDICIDiscoveredNode

**Framework**: Core MIDI  
**Kind**: class

A discovered MIDI-CI node that represents a MIDI source and destination that respond to capability inquiries.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MIDICIDiscoveredNode
```

## Topics

### Inspecting a Node
- [var destination: MIDIEntityRef](midicidiscoverednode/destination.md)
  The node’s MIDI destination.
- [var deviceInfo: MIDICIDeviceInfo](midicidiscoverednode/deviceinfo.md)
  The available MIDI-CI device information.
- [var supportsProfiles: Bool](midicidiscoverednode/supportsprofiles.md)
  A Boolean value that indicates whether this node supports MIDI-CI profiles.
- [var supportsProperties: Bool](midicidiscoverednode/supportsproperties.md)
  A Boolean value that indicates whether this node supports MIDI-CI properties.
- [var maximumSysExSize: NSNumber](midicidiscoverednode/maximumsysexsize.md)
  The maximum size of a System Exclusive (SysEx) message this node supports.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [typealias MIDICIDiscoveryResponseBlock](midicidiscoveryresponseblock.md)
  A block the system calls when a MIDI-CI node discovery request completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicidiscoverednode)*