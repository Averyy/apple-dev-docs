# MIDICIDiscoveryManager

**Framework**: Core MIDI  
**Kind**: class

A singleton object that performs systemwide MIDI-CI discovery.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MIDICIDiscoveryManager
```

#### Overview

Use this class to retrieve information about MIDI-CI–capable nodes in the MIDI subsystem. You can create [`MIDICISession`](midicisession.md) objects only from the destinations discovered using this API.

## Topics

### Accessing the Shared Instance
- [class func sharedInstance() -> MIDICIDiscoveryManager](midicidiscoverymanager/sharedinstance.md)
  Returns the singleton discovery manager instance.
### Discovering Nodes
- [func discover(handler: MIDICIDiscoveryResponseBlock)](midicidiscoverymanager/discover(handler:).md)
  Discovers the available MIDI-CI nodes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MIDICISession](midicisession.md)
  An object that represents a MIDI-CI session.
- [class MIDICIProfile](midiciprofile.md)
  A mapping of MIDI messages to specific sounds and synthesis behaviors, such as General MIDI, a drawbar organ, and so on.
- [class MIDICIProfileState](midiciprofilestate.md)
  An object that provides the enabled and disabled profiles for a MIDI channel or port on a device.
- [class MIDICIResponder](midiciresponder.md)
  An object that responds to MIDI-CI inquiries from an initiator on behalf of a MIDI client, and handles profile and property exchange operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicidiscoverymanager)*