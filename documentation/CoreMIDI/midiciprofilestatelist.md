# MIDICIProfileStateList

**Framework**: Core MIDI  
**Kind**: typealias  
**Role**: Type Alias

An array of profile state objects that describes the profile configuration for all channels of a reachable MIDI-CI node.

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
typedef NSArray<MIDICIProfileState *> MIDICIProfileStateList;
```

## See Also

### Capability Inquiry
- [class MIDICIDiscoveryManager](./midicidiscoverymanager.md)
  A singleton object that performs systemwide MIDI-CI discovery.
- [class MIDICISession](./midicisession.md)
  An object that represents a MIDI-CI session.
- [class MIDICIProfile](./midiciprofile.md)
  A mapping of MIDI messages to specific sounds and synthesis behaviors, such as General MIDI, a drawbar organ, and so on.
- [class MIDICIProfileState](./midiciprofilestate.md)
  An object that provides the enabled and disabled profiles for a MIDI channel or port on a device.
- [class MIDICIResponder](./midiciresponder.md)
  An object that responds to MIDI-CI inquiries from an initiator on behalf of a MIDI client, and handles profile and property exchange operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciprofilestatelist)*