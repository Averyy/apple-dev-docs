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
### Initializers
- [init?(coder: NSCoder)](midicidiscoverednode/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [typealias MIDICIDiscoveryResponseBlock](midicidiscoveryresponseblock.md)
  A block the system calls when a MIDI-CI node discovery request completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicidiscoverednode)*