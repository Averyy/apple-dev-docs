# MIDICIDiscoveryManager

**Framework**: Core MIDI  
**Kind**: class  
**Role**: Class

A singleton object that performs systemwide MIDI-CI discovery.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported for CoreMIDI

## Declaration

```swift
class MIDICIDiscoveryManager
```

```objc
@interface MIDICIDiscoveryManager : NSObject
```

#### Overview

Use this class to retrieve information about MIDI-CI–capable nodes in the MIDI subsystem. You can create [`MIDICISession`](./midicisession.md) objects only from the destinations discovered using this API.

## Topics

### Accessing the Shared Instance
- [class func sharedInstance() -> MIDICIDiscoveryManager](./midicidiscoverymanager/sharedinstance%28%29.md)
  Returns the singleton discovery manager instance.
### Discovering Nodes
- [func discover(handler: MIDICIDiscoveryResponseBlock)](./midicidiscoverymanager/discover%28handler%29.md)
  Discovers the available MIDI-CI nodes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Capability Inquiry
- [class MIDICISession](./midicisession.md)
  An object that represents a MIDI-CI session.
- [class MIDICIProfile](./midiciprofile.md)
  A mapping of MIDI messages to specific sounds and synthesis behaviors, such as General MIDI, a drawbar organ, and so on.
- [class MIDICIProfileState](./midiciprofilestate.md)
  An object that provides the enabled and disabled profiles for a MIDI channel or port on a device.
- [class MIDICIResponder](./midiciresponder.md)
  An object that responds to MIDI-CI inquiries from an initiator on behalf of a MIDI client, and handles profile and property exchange operations.
- [MIDICIProfileStateList](./midiciprofilestatelist.md)
  An array of profile state objects that describes the profile configuration for all channels of a reachable MIDI-CI node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicidiscoverymanager)*