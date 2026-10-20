# MIDICIDiscoveredNode

**Framework**: Core MIDI  
**Kind**: class  
**Role**: Class

A discovered MIDI-CI node that represents a MIDI source and destination that respond to capability inquiries.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported for CoreMIDI

## Declaration

```swift
class MIDICIDiscoveredNode
```

```objc
@interface MIDICIDiscoveredNode : NSObject
```

## Topics

### Inspecting a Node
- [var destination: MIDIEntityRef](./midicidiscoverednode/destination.md)
  The node’s MIDI destination.
- [var deviceInfo: MIDICIDeviceInfo](./midicidiscoverednode/deviceinfo.md)
  The available MIDI-CI device information.
- [var supportsProfiles: Bool](./midicidiscoverednode/supportsprofiles.md)
  A Boolean value that indicates whether this node supports MIDI-CI profiles.
- [var supportsProperties: Bool](./midicidiscoverednode/supportsproperties.md)
  A Boolean value that indicates whether this node supports MIDI-CI properties.
- [var maximumSysExSize: NSNumber](./midicidiscoverednode/maximumsysexsize.md)
  The maximum size of a System Exclusive (SysEx) message this node supports.
### Initializers
- [init?(coder: NSCoder)](./midicidiscoverednode/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Handling Callbacks
- [typealias MIDICIDiscoveryResponseBlock](./midicidiscoveryresponseblock.md)
  A block the system calls when a MIDI-CI node discovery request completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicidiscoverednode)*